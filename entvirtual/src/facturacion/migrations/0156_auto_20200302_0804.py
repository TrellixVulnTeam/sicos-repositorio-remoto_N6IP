# Generated by Django 2.2.4 on 2020-03-02 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0155_auto_20200302_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpp_arriendo',
            name='arriendo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.arriendo', verbose_name='Nombre del Tercero'),
        ),
    ]
