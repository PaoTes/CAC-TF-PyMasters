# Generated by Django 3.2.4 on 2023-12-02 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Descripcion', models.CharField(max_length=200)),
                ('Marca', models.CharField(max_length=20)),
            ],
        ),
    ]
