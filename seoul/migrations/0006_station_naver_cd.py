# Generated by Django 2.1.2 on 2018-10-31 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seoul', '0005_station_transfer_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='naver_cd',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]
