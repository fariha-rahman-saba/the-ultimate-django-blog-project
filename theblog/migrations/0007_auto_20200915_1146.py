# Generated by Django 3.1 on 2020-09-15 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_auto_20200915_1021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='lilkes',
            new_name='likes',
        ),
    ]
