# Generated by Django 2.2.4 on 2019-09-11 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0008_auto_20190911_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpp_arriendo_detalle',
            name='name_arri',
            field=models.IntegerField(max_length=150, null=True, verbose_name='Nombre Empresa'),
        ),
        migrations.AddField(
            model_name='cpp_arriendo_detalle',
            name='reten',
            field=models.FloatField(default=0, verbose_name='Retención'),
        ),
    ]
