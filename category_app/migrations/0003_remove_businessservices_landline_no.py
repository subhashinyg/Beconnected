# Generated by Django 2.2 on 2022-06-01 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category_app', '0002_locations_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessservices',
            name='landline_no',
        ),
    ]
