# Generated by Django 4.0.5 on 2022-07-05 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_supercategory_category_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='Rating',
            field=models.IntegerField(),
        ),
    ]
