# Generated by Django 2.2.4 on 2020-06-08 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cirugia', '0058_constante_smdlv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='honorario',
            name='info',
            field=models.TextField(blank=True, null=True, verbose_name='Información'),
        ),
    ]
