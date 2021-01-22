from django.db import models
from django.urls import reverse


class Contract(models.Model):

    # Порядковый номер договора
    number = models.CharField("№", max_length=3, default='')

    # Дата заключения договора
    contract_date = models.DateField(auto_now=False)

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
    contract_index = models.CharField("Индекс", max_length=3, default='')

    # Код отдела
    departament_code = models.IntegerField("Код отдела", default=0)

    # Полное название договора
    contract_full_name = models.CharField("Полное название договора", max_length=200, default='')

    # Автор регистрационной записи
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        null=True
    )

    # Переопредилим название модели на панели администратора
    class Meta:
        verbose_name = 'Договор'     # Для единственного числа
        verbose_name_plural = 'Договоры'      # Для множественного числа

    def __str__(self):
        return self.departament

    def get_absolute_url(self):
        return reverse('contract')
