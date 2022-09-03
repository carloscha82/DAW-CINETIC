# Generated by Django 4.1 on 2022-09-03 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinetic_app', '0010_rename_vende_boletas_boleta_venta_boleta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nacimiento',
            field=models.DateField(auto_now_add=True, default='2000-01-01'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='funcion',
            name='horario',
            field=models.TimeField(default='00:00'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listaventaproducto',
            name='venta_producto',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='cinetic_app.ventaproducto'),
            preserve_default=False,
        ),
    ]
