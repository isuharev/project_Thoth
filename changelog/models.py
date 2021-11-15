# -*- coding: utf-8 -*-
# 09.11.2021
# Если этот код работает, то его написал Сухарев-Крылов И.А., а если нет, то я не знаю, кто его написал
"""
    В этом файле описана модель таблицы,
которая будет хранить в себе историю изменений других таблиц.
"""
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Создадим сигналы для действий "создать", "удалить", "обновить"
ACTION_CREATE = 'create'
ACTION_UPDATE = 'update'
ACTION_DELETE = 'delete'


class ChangeLog(models.Model):
    TYPE_ACTION_ON_MODEL = (
        (ACTION_CREATE, _('Создание')),
        (ACTION_UPDATE, _('Обновление')),
        (ACTION_DELETE, _('Удаление')),
    )

    # Зададим поля таблицы
    changed = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата/Время изменения'
    )
    model = models.CharField(
        max_length=255,
        verbose_name='Таблица',
        null=True
    )
    record_id = models.IntegerField(
        verbose_name='id записи',
        null=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Автор изменения',
        on_delete=models.CASCADE,
        null=True
    )
    action_on_model = models.CharField(
        choices=TYPE_ACTION_ON_MODEL,
        max_length=50,
        verbose_name='Действие',
        null=True
    )
    before = models.TextField(
        verbose_name=u'Данные до изменения',
    )
    after = models.TextField(
        verbose_name=u'Данные после изменения',
    )
    ipaddress = models.CharField(
        max_length=15,
        verbose_name='IP адресс',
        null=True
    )

    class Meta:
        ordering = ('changed', )
        verbose_name = _('ChangeLog')
        verbose_name_plural = _('Change logs')

    def __str__(self):
        return f'{self.id}'

    @classmethod
    def add(cls, instance, user, ipaddress, action_on_model, old_data, new_data, id=None):
        # Этот метод отвечает за создание новой записи в таблице истрии изменений
        log = ChangeLog.objects.get(id=id) if id else ChangeLog()
        log.model = instance.__class__.__name__
        log.record_id = instance.pk
        if user:
            log.user = user
        log.ipaddress = ipaddress
        log.action_on_model = action_on_model
        log.before = old_data
        log.after = new_data
        log.save()
        return log.pk
