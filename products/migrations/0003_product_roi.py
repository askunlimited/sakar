# Generated by Django 3.0.7 on 2020-07-17 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ROI',
            field=models.FloatField(max_length=10, null=True),
        ),
    ]
