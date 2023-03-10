# Generated by Django 4.0.5 on 2023-01-05 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='father',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=33)),
                ('profession', models.CharField(max_length=44)),
            ],
        ),
        migrations.CreateModel(
            name='daughter',
            fields=[
                ('father_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='userapp.father')),
                ('age', models.IntegerField()),
            ],
            bases=('userapp.father',),
        ),
        migrations.CreateModel(
            name='son',
            fields=[
                ('father_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='userapp.father')),
                ('age', models.IntegerField()),
            ],
            bases=('userapp.father',),
        ),
    ]
