# Generated by Django 4.1.3 on 2022-12-10 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_remove_listing_location_listing_latitude_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='data_posted',
            new_name='date_posted',
        ),
    ]
