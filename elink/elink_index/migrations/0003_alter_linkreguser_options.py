# Generated by Django 3.2 on 2022-07-14 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elink_index', '0002_alter_linkreguser_linked'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='linkreguser',
            options={'ordering': ['-id']},
        ),
    ]
