# Generated by Django 2.0.2 on 2018-05-14 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvlist', '0002_auto_20180514_0306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tvshow',
            name='episodes',
        ),
        migrations.RemoveField(
            model_name='tvshow',
            name='watchedEpisodes',
        ),
        migrations.RemoveField(
            model_name='tvshow',
            name='year',
        ),
    ]
