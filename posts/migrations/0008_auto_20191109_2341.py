# Generated by Django 2.2.7 on 2019-11-09 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20191109_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'draft'), ('PUBLISHED', 'published')], default='published', max_length=10),
        ),
    ]
