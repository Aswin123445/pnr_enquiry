# Generated by Django 5.1.2 on 2024-10-19 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_fetch', '0002_pnr_source_station_pnr_train_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pnr',
            name='pnr',
            field=models.IntegerField(default=0),
        ),
    ]
