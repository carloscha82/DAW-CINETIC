# Generated by Django 4.1 on 2022-09-03 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinetic_app', '0004_rename_codigo_cinema_sala_cinema'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sala',
            old_name='cinema',
            new_name='cine',
        ),
    ]