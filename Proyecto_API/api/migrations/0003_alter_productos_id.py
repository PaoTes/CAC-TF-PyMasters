# Generated by Django 4.2.7 on 2023-12-05 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_productos_imagen_productos_precio_alter_productos_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]