# Generated by Django 4.0.5 on 2022-07-04 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('netPrice', models.DecimalField(decimal_places=2, max_digits=20)),
                ('paymentMode', models.CharField(choices=[('Pay On Delivery', 'Pay On Delivery'), ('Card', 'Card'), ('Online Payment', 'Online Payment')], default='Pay On Delivery', max_length=20)),
                ('Status', models.BooleanField(default=False)),
                ('deliveryAgent', models.IntegerField()),
            ],
        ),
    ]
