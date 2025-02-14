# Generated by Django 2.2.4 on 2020-03-16 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cirugia', '0004_auto_20200316_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='tiempo_proc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duracion_proc', models.FloatField(null=True, verbose_name='Duración del Procedimiento')),
                ('procedimiento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cirugia.procedimiento', verbose_name='Nombre del Procedimiento')),
                ('tipo_proc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cirugia.tipo_proc', verbose_name='Tipo Procedimiento')),
            ],
        ),
        migrations.DeleteModel(
            name='tiempo_procedimiento',
        ),
    ]
