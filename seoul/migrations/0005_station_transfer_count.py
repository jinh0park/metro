# Generated by Django 2.1.2 on 2018-10-29 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seoul', '0004_auto_20181027_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='transfer_count',
            field=models.IntegerField(default=1),
        ),
    ]
