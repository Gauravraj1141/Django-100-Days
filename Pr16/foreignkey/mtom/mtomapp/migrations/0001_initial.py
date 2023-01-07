# Generated by Django 4.0.5 on 2023-01-06 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('n_id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=44)),
                ('date', models.DateField(auto_now_add=True)),
                ('note', models.CharField(max_length=44)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
