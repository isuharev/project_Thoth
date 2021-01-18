from django.db import models
from django.urls import reverse


class Contract(models.Model):

    # Номер по списку
    number = models.IntegerField("№", default=0)

    # Дата заключения договора
    contract_date = models.DateField(auto_now=False)

    # Отдел
    departament = models.CharField("Отдел", max_length=200, default='')

    # Код (индекс) договора по номенклатуре дел
    contract_index = models.IntegerField("Индекс", default=0)

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
        return reverse('home')
