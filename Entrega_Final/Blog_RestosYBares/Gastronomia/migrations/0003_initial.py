# Generated by Django 4.1.3 on 2022-12-05 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Gastronomia', '0002_delete_bares_delete_restaurantes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('especialidad', models.CharField(max_length=100)),
                ('locacion', models.CharField(max_length=100)),
                ('horario_apertura', models.TimeField()),
                ('horario_cierre', models.TimeField()),
                ('breve_descripcion', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('especialidad', models.CharField(max_length=100)),
                ('locacion', models.CharField(max_length=100)),
                ('horario_apertura', models.TimeField()),
                ('horario_cierre', models.TimeField()),
                ('breve_descripcion', models.CharField(max_length=1000)),
            ],
        ),
    ]