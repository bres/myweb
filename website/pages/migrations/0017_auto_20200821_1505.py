# Generated by Django 3.1 on 2020-08-21 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_auto_20200820_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateField(auto_now=True),
        ),
    ]
