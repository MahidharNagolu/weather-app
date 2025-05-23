# Generated by Django 5.1.2 on 2024-10-22 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailySummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('avg_temperature', models.FloatField()),
                ('max_temperature', models.FloatField()),
                ('min_temperature', models.FloatField()),
                ('dominant_weather_condition', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('weather_condition', models.CharField(max_length=100)),
                ('temperature', models.FloatField()),
                ('feels_like', models.FloatField()),
                ('recorded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
