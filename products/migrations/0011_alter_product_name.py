# Generated by Django 4.0.5 on 2022-07-05 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_product_varients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Name',
            field=models.TextField(max_length=50),
        ),
    ]
