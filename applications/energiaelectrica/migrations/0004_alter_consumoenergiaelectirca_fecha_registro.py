# Generated by Django 3.2 on 2023-04-04 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energiaelectrica', '0003_alter_consumoenergiaelectirca_fecha_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumoenergiaelectirca',
            name='fecha_registro',
            field=models.DateField(),
        ),
    ]
