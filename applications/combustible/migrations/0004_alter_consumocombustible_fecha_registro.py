# Generated by Django 3.2 on 2023-04-01 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('combustible', '0003_alter_consumocombustible_fecha_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumocombustible',
            name='fecha_registro',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
