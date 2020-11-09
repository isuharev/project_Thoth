# Generated by Django 3.1.2 on 2020-11-09 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0007_entry_reg_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name': 'Запись в журнале', 'verbose_name_plural': 'Записи в журнале'},
        ),
        migrations.AddField(
            model_name='entry',
            name='departament',
            field=models.CharField(default='', max_length=200, verbose_name='Отдел'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='reg_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='reg_time',
            field=models.TimeField(auto_now=True),
        ),
    ]
