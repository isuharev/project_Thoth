# Generated by Django 3.1.2 on 2020-10-20 12:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0005_auto_20201020_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='reg_time',
        ),
        migrations.AlterField(
            model_name='entry',
            name='reg_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата регистрации документа'),
        ),
    ]
