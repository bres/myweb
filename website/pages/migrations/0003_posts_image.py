# Generated by Django 3.0.7 on 2020-07-07 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]