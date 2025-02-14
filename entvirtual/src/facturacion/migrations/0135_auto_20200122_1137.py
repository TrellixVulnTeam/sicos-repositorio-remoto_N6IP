# Generated by Django 2.2.4 on 2020-01-22 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0134_cpp_servi_detalle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuenta_aux',
            name='num_cuenta',
        ),
        migrations.RemoveField(
            model_name='cuenta_aux',
            name='serv_public',
        ),
        migrations.AddField(
            model_name='cuenta_aux',
            name='cuenta',
            field=models.CharField(max_length=50, null=True, verbose_name='Escriba Numero Cuenta'),
        ),
        migrations.AddField(
            model_name='cuenta_aux',
            name='naturaleza_cuenta',
            field=models.CharField(choices=[('Credito', 'Credito'), ('Debito', 'Debito')], default='Credito', max_length=8, verbose_name='Naturaleza de la Cuenta'),
        ),
        migrations.AddField(
            model_name='cuenta_aux',
            name='proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.proveedor', verbose_name='Seleccionar Proveedor'),
        ),
        migrations.AlterField(
            model_name='cuenta_aux',
            name='name_cuenta',
            field=models.CharField(max_length=50, null=True, verbose_name='Nombre de la Cuenta'),
        ),
        migrations.CreateModel(
            name='cuenta_aux_serv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cuenta', models.CharField(max_length=50, null=True, verbose_name='Nombre Cuenta')),
                ('num_cuenta', models.CharField(max_length=20, null=True, verbose_name='Número Cuenta')),
                ('serv_public', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.serv_public', verbose_name='Nombre del servicio')),
            ],
        ),
    ]
