# Generated by Django 3.1.2 on 2020-10-20 12:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0006_auto_20201020_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='reg_time',
            field=models.TimeField(default=datetime.time, verbose_name='Время регистрации документа'),
        ),
    ]
