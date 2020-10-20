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

    # Дата и время регистрации записи
    reg_date = models.DateField("Дата регистрации документа", default=datetime.date.today)
    reg_time = models.TimeField("Время регистрации документа", default=datetime.time)

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

    # как работает эта хрень, я до конца не разобрался
    # TODO: надо посмотреть матчасть
    # Вроде как она позволяет отсылаться к определённому объекту через название его URL маршрута
    def get_absolute_url(self):
        return reverse('home')
