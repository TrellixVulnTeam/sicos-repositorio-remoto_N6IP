# Generated by Django 2.2.4 on 2020-03-24 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cirugia', '0015_auto_20200324_1114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipo_proc',
            options={'ordering': ['nombre_tipo_proc']},
        ),
        migrations.AddField(
            model_name='procedimiento',
            name='duracion_proc',
            field=models.FloatField(null=True, verbose_name='Duración del Procedimiento'),
        ),
        migrations.DeleteModel(
            name='tiempo_proc',
        ),
    ]
