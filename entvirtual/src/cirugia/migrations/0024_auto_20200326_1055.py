# Generated by Django 2.2.4 on 2020-03-26 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cirugia', '0023_remove_canasta_tipo_proc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canasta',
            name='costo_tot',
            field=models.FloatField(default=0, null=True, verbose_name='Costo Subtotal'),
        ),
    ]
