# Generated by Django 5.0 on 2023-12-10 03:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0002_huesped_alter_habitacion_numero_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='total_pagar',
        ),
        migrations.AddField(
            model_name='reserva',
            name='tipo_habitacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel_app.tipohabitacion'),
        ),
    ]
