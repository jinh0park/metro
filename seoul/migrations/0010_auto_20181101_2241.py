# Generated by Django 2.1.2 on 2018-11-01 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seoul', '0009_station_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='station',
            old_name='id',
            new_name='index',
        ),
    ]
