# Generated by Django 3.0.3 on 2020-02-13 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20200213_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='publish',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания записи'),
        ),
    ]