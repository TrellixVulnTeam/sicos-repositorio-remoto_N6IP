# Generated by Django 2.2.4 on 2020-03-20 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cirugia', '0011_auto_20200320_1004'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='actividad',
            new_name='position',
        ),
        migrations.RenameField(
            model_name='canasta',
            old_name='actividad',
            new_name='position',
        ),
        migrations.RenameField(
            model_name='salario',
            old_name='actividad',
            new_name='position',
        ),
    ]
