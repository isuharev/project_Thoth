# Generated by Django 3.1.2 on 2021-02-18 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0016_auto_20210218_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='departament_code',
            field=models.CharField(default='', max_length=100, verbose_name='Код отдела'),
        ),
    ]
