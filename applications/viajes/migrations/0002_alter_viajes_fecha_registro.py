# Generated by Django 3.2 on 2023-04-01 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viajes',
            name='fecha_registro',
            field=models.DateField(auto_now_add=True),
        ),
    ]
