# Generated by Django 2.2 on 2022-06-27 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category_app', '0009_remove_businessservices_landphone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessservices',
            name='fax',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='businessservices',
            name='googlemap',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='businessservices',
            name='linkedin',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='businessservices',
            name='watsapp',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
