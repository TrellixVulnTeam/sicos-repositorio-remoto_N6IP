# Generated by Django 2.2.4 on 2020-02-19 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0136_auto_20200122_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='distri_serv_public',
            name='boolean',
            field=models.BooleanField(default=False),
        ),
    ]
