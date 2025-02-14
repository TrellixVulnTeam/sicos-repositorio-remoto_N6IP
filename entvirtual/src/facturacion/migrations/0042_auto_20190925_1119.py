# Generated by Django 2.2.4 on 2019-09-25 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0041_fac_especialista_detalle_glosa'),
    ]

    operations = [
        migrations.CreateModel(
            name='retencion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('honorario', models.FloatField(default=0, null=True, verbose_name='Honorario')),
                ('incr_aport_pension', models.FloatField(default=0, null=True, verbose_name='Aportes a Pension')),
                ('incr_solida_pensional', models.FloatField(default=0, null=True, verbose_name='Solidaridad Pensional')),
                ('incr_aport_salud', models.FloatField(default=0, null=True, verbose_name='Aportes a Salud')),
                ('incr_aport_arl', models.FloatField(default=0, null=True, verbose_name='Aportes a ARL')),
                ('incr_aport_vol_pension', models.FloatField(default=0, null=True, verbose_name='Aportes Voluntaios a Pension')),
                ('deduc_int_prest_vivienda', models.FloatField(default=0, null=True, verbose_name='Intereses Prestamo Viviendas')),
                ('deduc_plan_comp_salud', models.FloatField(default=0, null=True, verbose_name='Plan Complementario Salud')),
                ('deduc_depen_cargo', models.FloatField(default=0, null=True, verbose_name='Dependinte de Cargo')),
                ('re_deduc_rent_exent', models.FloatField(default=0, null=True, verbose_name='Total Deducciones + Renta Exenta')),
                ('re_rent_exent_lab', models.FloatField(default=0, null=True, verbose_name='Tope Deducciones + Renta Exenta')),
                ('re_total_base_grav_reten', models.FloatField(default=0, null=True, verbose_name='Total Base Gravable para Retención')),
                ('re_base_grav_reten_uvt', models.FloatField(default=0, null=True, verbose_name='Valor Retención en UVT')),
                ('re_valor_reten', models.FloatField(default=0, null=True, verbose_name='Valor Retención')),
            ],
        ),
        migrations.RemoveField(
            model_name='fac_especialista_detalle',
            name='deduc_depen_cargo',
        ),
        migrations.RemoveField(
            model_name='fac_especialista_detalle',
            name='deduc_int_prest_vivienda',
        ),
        migrations.RemoveField(
            model_name='fac_especialista_detalle',
            name='deduc_plan_comp_salud',
        ),
        migrations.RemoveField(
            model_name='fac_especialista_detalle',
            name='honorario',
        ),
        migrations.RemoveField(
            model_name='fac_especialista_detalle',
            name='incr_aport_arl',
        ),
        migrations.RemoveField(
            model_name='fac_especialista_detalle',
            name='incr_aport_pension',
        ),
        migrations.RemoveField(
            model_name='fac_especialista_detalle',
            name='incr_aport_salud',
        ),
        migrations.RemoveField(
            model_name='fac_especialista_detalle',
            name='incr_aport_vol_pension',
        ),
        migrations.RemoveField(
            model_name='fac_especialista_detalle',
            name='incr_solida_pensional',
        ),
        migrations.RemoveField(
            model_name='fac_especialista_detalle',
            name='re_base_grav_reten_uvt',
        ),
        migrations.RemoveField(
            model_name='fac_especialista_detalle',
            name='re_deduc_rent_exent',
        ),
        migrations.RemoveField(
            model_name='fac_especialista_detalle',
            name='re_rent_exent_lab',
        ),
        migrations.RemoveField(
            model_name='fac_especialista_detalle',
            name='re_total_base_grav_reten',
        ),
        migrations.RemoveField(
            model_name='fac_especialista_detalle',
            name='re_valor_reten',
        ),
    ]
