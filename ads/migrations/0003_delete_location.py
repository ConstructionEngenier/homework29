# Generated by Django 4.0.5 on 2022-07-03 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_location_alter_ad_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Location',
        ),
    ]
