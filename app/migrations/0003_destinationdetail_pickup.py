# Generated by Django 5.0.6 on 2024-06-09 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_destinationdetail_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='destinationdetail',
            name='pickup',
            field=models.CharField(default='test', max_length=40),
            preserve_default=False,
        ),
    ]
