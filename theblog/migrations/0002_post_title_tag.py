# Generated by Django 3.0.8 on 2020-07-20 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='My Freakin Blog', max_length=255),
        ),
    ]
