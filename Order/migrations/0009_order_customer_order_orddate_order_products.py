# Generated by Django 4.0.5 on 2022-07-08 03:55

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Order', '0008_remove_order_customer_remove_order_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='ordDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 8, 9, 25, 18, 395853)),
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='Order.products'),
        ),
    ]
