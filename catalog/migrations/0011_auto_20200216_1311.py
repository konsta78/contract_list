# Generated by Django 3.0.2 on 2020-02-16 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20200213_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='person',
            field=models.CharField(choices=[('1', 'Павлышко Екатерина Сергеевна'), ('2', 'Пуленкова Римма Николаевна'), ('3', 'Бочков Максим Александрович'), ('4', 'Великородная Оксана Леонидовна')], default='Павлышко Е. С.', max_length=20, verbose_name='Контактное лицо ДО'),
        ),
    ]
