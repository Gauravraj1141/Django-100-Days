# Generated by Django 4.0.5 on 2023-01-29 08:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_alter_users_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_id',
            field=models.BigAutoField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False),
        ),
    ]