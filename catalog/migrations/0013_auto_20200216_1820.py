# Generated by Django 3.0.2 on 2020-02-16 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20200216_1438'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='managerperson',
            options={'ordering': ['manager_name']},
        ),
    ]
