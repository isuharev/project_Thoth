# Generated by Django 3.1.2 on 2021-01-22 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0008_contract_registration_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='contract_cost',
            field=models.CharField(default='', max_length=200, verbose_name='Стоимость'),
        ),
        migrations.AddField(
            model_name='contract',
            name='contract_status',
            field=models.CharField(default='', max_length=200, verbose_name='Статус договора'),
        ),
        migrations.AddField(
            model_name='contract',
            name='executor',
            field=models.CharField(default='', max_length=200, verbose_name='Исполнитель'),
        ),
    ]
