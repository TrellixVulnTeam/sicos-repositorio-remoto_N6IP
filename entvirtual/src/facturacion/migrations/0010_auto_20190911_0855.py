# Generated by Django 2.2.4 on 2019-09-11 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0009_auto_20190911_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpp_arriendo_detalle',
            name='name_arri',
            field=models.CharField(max_length=150, null=True, verbose_name='Nombre Empresa'),
        ),
    ]
