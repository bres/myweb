# Generated by Django 3.1 on 2020-08-21 15:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20200821_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 21, 15, 9, 28, 571806)),
        ),
    ]
