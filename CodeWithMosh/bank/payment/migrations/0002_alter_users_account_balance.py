# Generated by Django 4.0.5 on 2023-01-29 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='account_balance',
            field=models.BigIntegerField(),
        ),
    ]