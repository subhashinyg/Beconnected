# Generated by Django 2.2 on 2022-06-06 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category_app', '0007_businessservices'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privacy', models.CharField(max_length=500)),
            ],
        ),
    ]
