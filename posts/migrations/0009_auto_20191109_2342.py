# Generated by Django 2.2.7 on 2019-11-09 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20191109_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('PUBLISHED', 'published'), ('DRAFT', 'draft')], default='published', max_length=10),
        ),
    ]
