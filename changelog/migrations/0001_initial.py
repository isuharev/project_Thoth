# Generated by Django 3.1.2 on 2021-11-09 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changed', models.DateTimeField(auto_now=True, verbose_name='Дата/Время изменения')),
                ('model', models.CharField(max_length=255, null=True, verbose_name='Таблица')),
                ('record_id', models.IntegerField(null=True, verbose_name='id записи')),
                ('action_on_model', models.CharField(choices=[('create', 'Создание'), ('update', 'Обновление'), ('delete', 'Удаление')], max_length=50, null=True, verbose_name='Действие')),
                ('data', models.JSONField(default=dict, verbose_name='Изменяемые данные модели')),
                ('ipaddress', models.CharField(max_length=15, null=True, verbose_name='IP адресс')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор изменения')),
            ],
            options={
                'verbose_name': 'ChangeLog',
                'verbose_name_plural': 'Change logs',
                'ordering': ('changed',),
            },
        ),
    ]