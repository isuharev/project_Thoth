# Generated by Django 3.1.2 on 2021-01-18 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0008_auto_20201109_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='number_out',
            field=models.CharField(default='', max_length=64, verbose_name='№ исх.'),
        ),
    ]