# Generated by Django 3.1.3 on 2020-11-11 13:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATM', '0008_auto_20201111_0801'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='account_number',
            new_name='account_name',
        ),
        migrations.AlterField(
            model_name='card',
            name='exp_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 11, 8, 10, 0, 388235)),
        ),
    ]
