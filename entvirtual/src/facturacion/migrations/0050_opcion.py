# Generated by Django 2.2.4 on 2019-10-18 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0049_auto_20191018_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='opcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcion', models.CharField(max_length=2, null=True, verbose_name='Opción')),
            ],
        ),
    ]
