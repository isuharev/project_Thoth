# Generated by Django 3.1.2 on 2021-01-22 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0011_auto_20210122_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contract_date',
            field=models.DateField(),
        ),
    ]
