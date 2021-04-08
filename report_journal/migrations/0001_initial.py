# Generated by Django 3.1.2 on 2021-04-06 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default='', max_length=300, verbose_name='№')),
            ],
            options={
                'verbose_name': 'Отчётный документ',
                'verbose_name_plural': 'Отчётные документы',
            },
        ),
    ]
