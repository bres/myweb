# Generated by Django 3.1 on 2020-08-20 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20200818_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Blog_title_tag',
            field=models.CharField(max_length=200),
        ),
    ]