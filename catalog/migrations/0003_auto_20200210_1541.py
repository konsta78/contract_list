# Generated by Django 3.0.2 on 2020-02-10 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200210_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='date_work_note',
            field=models.DateField(blank=True, null=True, verbose_name='Дата служебной записки'),
        ),
        migrations.AddField(
            model_name='contract',
            name='num_work_note',
            field=models.IntegerField(blank=True, max_length=3, null=True, verbose_name='Номер служебной записки'),
        ),
        migrations.AlterField(
            model_name='constructionobject',
            name='line',
            field=models.CharField(choices=[('НВЛ', 'Невско-Василеостровская линия'), ('Ф-2', 'Фрунзенский радиус'), ('ЛПЛ', 'Лахтинско-Правобережная линиия'), ('ККЛ', 'Красносельско-Калининская линия'), ('Другое', 'Другое')], default='Другое', max_length=50, verbose_name='Объект строительства'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='constr_object',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ConstructionObject_constr_object', to='catalog.ConstructionObject', verbose_name='Объект строительства'),
        ),
    ]