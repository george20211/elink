# Generated by Django 3.2 on 2022-07-14 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elink_index', '0003_alter_linkreguser_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='infolink',
            name='device',
            field=models.SmallIntegerField(db_index=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='infolink',
            name='country_check',
            field=models.SmallIntegerField(db_index=True),
        ),
    ]
