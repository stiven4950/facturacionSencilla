# Generated by Django 3.0.3 on 2021-02-14 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='identity',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
    ]