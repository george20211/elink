# Generated by Django 3.2 on 2022-07-14 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elink_index', '0005_auto_20220714_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkreguser',
            name='public_stat',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]