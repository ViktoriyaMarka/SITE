# Generated by Django 3.1.4 on 2020-12-12 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system_app',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Наименование требований'),
        ),
        migrations.AlterField(
            model_name='system_prog',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Наименование требований'),
        ),
    ]
