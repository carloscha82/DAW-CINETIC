# Generated by Django 4.1 on 2022-09-03 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinetic_app', '0008_alter_listaventaproducto_combo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listaventaproducto',
            name='combo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cinetic_app.combo'),
        ),
        migrations.AlterField(
            model_name='listaventaproducto',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cinetic_app.producto'),
        ),
    ]
