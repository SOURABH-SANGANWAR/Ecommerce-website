# Generated by Django 4.0.5 on 2022-07-04 05:24

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=50, unique=True)),
                ('Image', models.ImageField(default='default_prduct.jpg', upload_to=products.models.Product_img)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('MRP', models.DecimalField(decimal_places=2, max_digits=20)),
                ('Rating', models.DecimalField(decimal_places=1, max_digits=2, null=True)),
                ('category', models.CharField(choices=[('Electronics', 'Electronics'), ('Groceries', 'Groceries'), ('Eatbles', 'Eatbles'), ('Unknown', 'Unknown')], default='Unknown', max_length=20)),
            ],
        ),
    ]