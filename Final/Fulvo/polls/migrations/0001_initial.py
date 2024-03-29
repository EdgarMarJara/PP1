# Generated by Django 4.1.5 on 2023-08-04 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Canchas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo', models.CharField(max_length=100)),
                ('Ciudad', models.CharField(max_length=100)),
                ('Departamento', models.CharField(max_length=100)),
                ('Hora_abre', models.TimeField()),
                ('Hora_cerra', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hora_Inicio', models.TimeField()),
                ('Hora_Fin', models.TimeField()),
                ('ID_cancha', models.ForeignKey(blank=True, db_column='ID_cancha', null=True, on_delete=django.db.models.deletion.PROTECT, to='polls.canchas')),
            ],
        ),
        migrations.CreateModel(
            name='Gestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estado', models.CharField(max_length=20)),
                ('Recomendacion', models.CharField(max_length=200)),
                ('H_in', models.TimeField()),
                ('H_out', models.TimeField()),
                ('ID_Reserva', models.ForeignKey(blank=True, db_column='ID_Reserva', null=True, on_delete=django.db.models.deletion.PROTECT, to='polls.reserva')),
            ],
        ),
    ]
