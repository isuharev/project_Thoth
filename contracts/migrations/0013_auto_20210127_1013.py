# Generated by Django 3.1.2 on 2021-01-27 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0012_auto_20210122_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contract_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]