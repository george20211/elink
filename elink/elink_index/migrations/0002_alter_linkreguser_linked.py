# Generated by Django 3.2 on 2022-07-13 19:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elink_index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkreguser',
            name='linked',
            field=models.TextField(max_length=5000, validators=[django.core.validators.URLValidator()]),
        ),
    ]