# Generated by Django 2.2 on 2022-05-17 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_profile_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop_profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterModelTable(
            name='shop_profile',
            table='Shop_profile',
        ),
    ]
