# Generated by Django 4.0.5 on 2022-07-09 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Colours',
            field=models.ManyToManyField(blank=True, to='products.colour'),
        ),
    ]