# Generated by Django 5.1.2 on 2024-10-24 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0006_alertpreference_humidity_threshold_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailysummary',
            name='max_wind_speed',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
