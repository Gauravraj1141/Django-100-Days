# Generated by Django 4.0.5 on 2023-01-11 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZoneSchools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=33)),
                ('address', models.CharField(max_length=55)),
                ('Contact_no', models.CharField(max_length=33)),
            ],
        ),
    ]
