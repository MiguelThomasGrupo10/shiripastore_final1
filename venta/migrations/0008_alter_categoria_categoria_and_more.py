# Generated by Django 4.1.2 on 2023-06-14 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0007_alter_categoria_id_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='categoria',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='plataforma',
            name='plataforma',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
