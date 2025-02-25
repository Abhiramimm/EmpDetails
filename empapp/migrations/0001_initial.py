# Generated by Django 5.0.6 on 2024-07-05 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('mobile_number', models.PositiveIntegerField()),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empapp.category')),
            ],
        ),
    ]
