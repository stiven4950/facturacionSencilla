# Generated by Django 3.0.3 on 2021-02-14 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_profile_adress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='adress',
            new_name='address',
        ),
    ]
