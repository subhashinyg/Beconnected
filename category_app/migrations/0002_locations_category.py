# Generated by Django 2.2 on 2022-05-30 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='locations',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='category_app.Category'),
            preserve_default=False,
        ),
    ]
