# Generated by Django 2.1.2 on 2018-10-31 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seoul', '0006_station_naver_cd'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='head_station',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='head_station_set', to='seoul.Station'),
        ),
        migrations.AddField(
            model_name='station',
            name='tail_station',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='tail_station_set', to='seoul.Station'),
        ),
    ]
