# Generated by Django 3.2 on 2023-04-04 05:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('combustible', '0005_alter_consumocombustible_fecha_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumocombustible',
            name='fecha_registro',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
