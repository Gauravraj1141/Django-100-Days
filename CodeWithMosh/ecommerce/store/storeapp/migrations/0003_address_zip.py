# Generated by Django 4.0.5 on 2023-01-23 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0002_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.IntegerField(default='222'),
            preserve_default=False,
        ),
    ]