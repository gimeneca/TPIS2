# Generated by Django 3.1 on 2020-08-18 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0002_auto_20200818_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_inicio',
            field=models.DateField(),
        ),
    ]
