from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.urls import reverse
from django.db import models
from changelog.mixins import ChangeloggableMixin
from changelog.signals import journal_save_handler, journal_delete_handler
from django.db.models.signals import post_delete, post_save
import hashlib
import os


def upload_to(instance, filename, fieldname='document'):
    ext = os.path.splitext(filename)[1].lower()
    class_name = instance.__class__.__name__.lower()

    h = hashlib.sha256()
    field = getattr(instance, fieldname)
    for chunk in field.chunks():
        h.update(chunk)
    name = h.hexdigest()

    return os.path.join(
        class_name,
        name + ext,
    )


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


class Contract(ChangeloggableMixin, models.Model):
    # Порядковый номер договора
    number = models.CharField("№", max_length=300, default='')

    # Дата заключения договора
    contract_date = models.DateField("Дата заключения договора", auto_now=False, blank=True, null=True)

    # Контрагент, с которым заключён договор
    contract_agent = models.CharField("Контрагент:", max_length=200, default='')

    # Исполнитель договора
    executor = models.CharField("Исполнитель", max_length=200, default='')

    # Стоимость контракта
    contract_cost = models.CharField("Стоимость", max_length=200, default='')

    # Статус контракта
    contract_status = models.CharField("Статус договора", max_length=200, default='')

    # Дата регистрации договора в системе
    registration_date = models.DateField(auto_now=True)

    # Отдел
    departament = models.CharField("Отдел", max_length=200, default='')

    # Код (индекс) договора по номенклатуре дел
    contract_index = models.CharField("Индекс", max_length=3, default='', blank=True)

    # Код отдела
    departament_code = models.CharField("Код отдела", max_length=100, default='')

    # Полное название договора
    contract_full_name = models.CharField("Полное название договора", max_length=200, default='')

    # Файл договора и дата его подгрузки
    document = models.FileField(
        storage=OverwriteStorage(),
        upload_to=upload_to,
        default='',
        blank=True
    )
    uploaded_at = models.DateTimeField(auto_now=True)

    # Автор регистрационной записи
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        null=True
    )

    # Переопредилим название модели на панели администратора
    class Meta:
        verbose_name = 'Договор'  # Для единственного числа
        verbose_name_plural = 'Договоры'  # Для множественного числа

    def __str__(self):
        return self.departament

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


post_save.connect(journal_save_handler, sender=Contract)
post_delete.connect(journal_delete_handler, sender=Contract)
