# Generated by Django 3.0.3 on 2020-02-12 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excursion',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
