# Generated by Django 2.2.4 on 2020-04-04 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0186_auto_20200404_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpp_proveedor',
            name='option',
            field=models.BooleanField(default=True, verbose_name='¿Parametrizado?'),
        ),
        migrations.AddField(
            model_name='cpp_proveedor',
            name='valor_factura',
            field=models.FloatField(default=0, verbose_name='Valor Factura'),
        ),
    ]
