# Generated by Django 2.2.7 on 2019-11-08 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_profile_simage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='simage',
        ),
    ]
