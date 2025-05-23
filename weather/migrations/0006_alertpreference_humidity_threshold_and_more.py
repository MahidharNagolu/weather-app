# Generated by Django 5.1.2 on 2024-10-23 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0005_remove_weather_feels_like_dailysummary_avg_humidity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alertpreference',
            name='humidity_threshold',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alertpreference',
            name='wind_speed_threshold',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alertpreference',
            name='temperature_threshold',
            field=models.FloatField(),
        ),
    ]
