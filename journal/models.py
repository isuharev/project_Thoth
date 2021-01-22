from django.db import models
from django.urls import reverse
import datetime


class Entry(models.Model):
    """
    Этот класс описывает модель записи в журнал регистрации документов.
    Она описывает поля, содержащиеся в этой модели (т.е. фактически создаёт соотвествующие столбцы в базе данных)
    """
    # Номер по списку
    number = models.IntegerField("№", default=0)

    # Дата и время регистрации записи (эти поля модели заполняются автоматически, скрыто от пользователя)
    reg_date = models.DateField(auto_now=True)
    reg_time = models.TimeField(auto_now=True)

    # № исх.
    number_out = models.CharField("№ исх.", max_length=64, default='')

    # Адресант документа, для которого создаётся регистрационная запись
    to_whom = models.CharField("Кому", max_length=200, default='')

    # Содержание документа
    what = models.CharField("Содержание", max_length=200, default='')

    # Исполнитель документа
    executor = models.CharField("Исполнитель", max_length=200, default='')

    # Автор регистрационной записи
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )

    # Отдел
    departament = models.CharField("Отдел", max_length=200, default='')

    # Переопредилим название модели на панели администратора
    class Meta:
        verbose_name = 'Запись в журнале'     # Для единственного числа
        verbose_name_plural = 'Записи в журнале'      # Для множественного числа

    def __str__(self):
        return self.number_out

    # как работает эта хрень, я до конца не разобрался
    # TODO: надо посмотреть матчасть
    # Вроде как она позволяет отсылаться к определённому объекту через название его URL маршрута
    def get_absolute_url(self):
        return reverse('home', kwargs={'pk': self.pk})
