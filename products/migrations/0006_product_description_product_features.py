# Generated by Django 4.0.5 on 2022-07-04 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_review_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='Will be updated Soon', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='features',
            field=models.TextField(blank=True, default='Will be updated Soon', null=True),
        ),
    ]