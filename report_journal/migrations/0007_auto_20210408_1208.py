# Generated by Django 3.1.2 on 2021-04-08 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_journal', '0006_auto_20210408_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата'),
        ),
    ]