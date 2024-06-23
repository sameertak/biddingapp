# Generated by Django 5.0.6 on 2024-06-23 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_bid_accepted_by_bid_is_accepted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='is_accepted',
        ),
        migrations.AddField(
            model_name='bid',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=10),
        ),
    ]
