# Generated by Django 3.0.8 on 2020-07-14 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alimenti', '0002_auto_20200714_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alimento',
            name='diete',
        ),
        migrations.DeleteModel(
            name='Dieta',
        ),
    ]