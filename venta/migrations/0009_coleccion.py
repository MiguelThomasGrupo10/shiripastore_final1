# Generated by Django 4.1.2 on 2023-06-29 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0008_alter_categoria_categoria_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coleccion',
            fields=[
                ('Id_coleccion', models.AutoField(db_column='idColeccion', primary_key=True, serialize=False)),
                ('coleccion', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]