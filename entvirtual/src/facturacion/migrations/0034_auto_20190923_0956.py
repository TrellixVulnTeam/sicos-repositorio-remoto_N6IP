# Generated by Django 2.2.4 on 2019-09-23 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0033_auto_20190923_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='especialista',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.especialista', verbose_name='Nombre del Especialista'),
        ),
    ]
