# Generated by Django 4.0.5 on 2022-07-09 01:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0016_alter_order_orddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 9, 6, 38, 3, 390469)),
        ),
    ]
