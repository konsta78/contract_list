# Generated by Django 3.0.2 on 2020-02-11 20:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20200210_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
