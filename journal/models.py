from django.db import models


class Entry(models.Model):

    # Номер по списку
    number = models.IntegerField("№", default=0)

    # Дата и время регистрации записи
    date_time = models.DateTimeField("Дата и время регистрации")

    # № исх.
    number_out = models.CharField("№ исх.", max_length=64, default=0)

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

    def __str__(self):
        return self.number_out

