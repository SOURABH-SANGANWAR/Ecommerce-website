# Generated by Django 4.0.5 on 2022-07-08 10:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0011_alter_order_orddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 8, 16, 19, 30, 902270)),
        ),
    ]
