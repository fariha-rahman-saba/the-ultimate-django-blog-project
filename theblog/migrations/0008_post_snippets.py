# Generated by Django 3.1 on 2020-09-19 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0007_auto_20200915_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippets',
            field=models.CharField(default='click on post to view', max_length=255),
        ),
    ]
