# Generated by Django 2.2.4 on 2020-03-26 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cirugia', '0019_auto_20200326_0955'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='concepto_canasta',
            options={'ordering': ['nombre_canasta']},
        ),
        migrations.AlterModelOptions(
            name='concepto_honorario',
            options={'ordering': ['nombre_concep_hon']},
        ),
        migrations.AlterModelOptions(
            name='concepto_salario',
            options={'ordering': ['nombre_concep_sal']},
        ),
        migrations.AlterModelOptions(
            name='constante',
            options={'ordering': ['iss_adicional']},
        ),
        migrations.AlterModelOptions(
            name='nombre_canasta',
            options={'ordering': ['nombre_canasta']},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ['nombre_act']},
        ),
        migrations.AlterModelOptions(
            name='procedimiento',
            options={'ordering': ['nombre_proc']},
        ),
        migrations.AlterModelOptions(
            name='rubro',
            options={'ordering': ['nombre_rubro']},
        ),
    ]
