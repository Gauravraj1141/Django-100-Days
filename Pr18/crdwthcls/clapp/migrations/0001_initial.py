# Generated by Django 4.0.5 on 2023-01-10 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('UsId', models.BigAutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=100)),
                ('Phone', models.CharField(max_length=20)),
                ('Date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
