# Generated by Django 3.2 on 2022-07-14 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elink_index', '0004_auto_20220714_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infolink',
            old_name='country_check',
            new_name='country_check_id',
        ),
        migrations.RenameField(
            model_name='infolink',
            old_name='device',
            new_name='device_id',
        ),
    ]
