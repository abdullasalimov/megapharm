# Generated by Django 3.2.9 on 2022-04-18 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_product_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
