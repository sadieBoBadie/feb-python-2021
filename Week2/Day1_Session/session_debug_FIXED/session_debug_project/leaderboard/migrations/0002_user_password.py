# Generated by Django 2.2.4 on 2021-02-17 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='password123', max_length=255),
            preserve_default=False,
        ),
    ]
