# Generated by Django 4.0.5 on 2023-01-23 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0003_address_zip'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['last_name', 'first_name'], name='storeapp_cu_last_na_36b225_idx'),
        ),
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['first_name'], name='user_first_name_for_store'),
        ),
    ]