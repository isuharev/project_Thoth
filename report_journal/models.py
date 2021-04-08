from django.urls import reverse
from django.db import models


class Reports(models.Model):

    # Порядковый номер договора
    number = models.CharField("№", max_length=300, blank=True, default='б/н')
    date = models.DateField("Дата", auto_now=False, blank=True, null=True)
    doc_number = models.CharField("№ документа", max_length=64, default='')
    doc = models.CharField("Документ", max_length=64, default='')
    from_to = models.CharField("От кого/кому", max_length=64, default='')
    what = models.CharField("Содержание", max_length=200, default='')
    comment = models.CharField("Примечание", max_length=200, blank=True, default='')
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        null=True
    )

    # Переопредилим название модели на панели администратора
    class Meta:
        verbose_name = 'Отчётный документ'     # Для единственного числа
        verbose_name_plural = 'Отчётные документы'      # Для множественного числа

    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return reverse('reports')
