# Generated by Django 2.2.4 on 2020-01-03 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0099_auto_20200103_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpp_proveedor_detalle',
            name='distribucion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.distribucion', verbose_name='Producto'),
        ),
    ]
