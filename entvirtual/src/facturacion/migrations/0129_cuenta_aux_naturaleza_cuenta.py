# Generated by Django 2.2.4 on 2020-01-13 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0128_auto_20200113_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuenta_aux',
            name='naturaleza_cuenta',
            field=models.CharField(choices=[('Credito', 'Credito'), ('Debito', 'Debito')], default='Credito', max_length=8, verbose_name='Naturaleza de la Cuenta'),
        ),
    ]
