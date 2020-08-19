# Generated by Django 3.1 on 2020-08-18 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=4, unique=True)),
                ('fecha_inicio', models.DateField(auto_now_add=True)),
                ('fecha_fin', models.DateField()),
                ('estado', models.CharField(choices=[('PEN', 'PENDIENTE'), ('TER', 'TERMINADO'), ('CUR', 'CURSO')], max_length=3)),
                ('Sprint', models.DateTimeField()),
                ('tarea', models.CharField(max_length=50)),
                ('cliente', models.CharField(max_length=50)),
            ],
        ),
    ]
