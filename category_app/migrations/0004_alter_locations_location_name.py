# Generated by Django 4.0.2 on 2022-04-11 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category_app', '0003_locations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='location_name',
            field=models.CharField(max_length=100),
        ),
    ]
