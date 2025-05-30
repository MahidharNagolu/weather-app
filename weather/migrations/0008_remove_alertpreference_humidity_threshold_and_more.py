# Generated by Django 5.1.2 on 2024-10-25 04:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0007_dailysummary_max_wind_speed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alertpreference',
            name='humidity_threshold',
        ),
        migrations.RemoveField(
            model_name='alertpreference',
            name='wind_speed_threshold',
        ),
        migrations.AddField(
            model_name='alertpreference',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='alertpreference',
            name='weather_condition',
            field=models.CharField(choices=[('temperature', 'Temperature'), ('humidity', 'Humidity')], default=0, max_length=50),
            preserve_default=False,
        ),
    ]
