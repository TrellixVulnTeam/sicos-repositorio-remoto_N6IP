# Generated by Django 2.2.4 on 2020-02-19 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0142_auto_20200219_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpp_serv_public',
            name='iva',
            field=models.FloatField(default=0, null=True, verbose_name='% Iva'),
        ),
    ]
