# Generated by Django 4.0.5 on 2022-07-04 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='TransactionId',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.TextField(null=True),
        ),
    ]
