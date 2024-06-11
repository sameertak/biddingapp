# Generated by Django 5.0.6 on 2024-06-10 06:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_vehicledetails_loading_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='destinationdetail',
            name='time_limit',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 10, 6, 6, 49, 442493)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='destinationdetail',
            name='number_of_vehicles',
            field=models.IntegerField(default=1),
        ),
    ]