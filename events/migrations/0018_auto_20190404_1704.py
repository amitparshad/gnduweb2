# Generated by Django 2.1.7 on 2019-04-04 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_event_event_organisers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.AddField(
            model_name='event',
            name='date_time',
            field=models.DateTimeField(null=True),
        ),
    ]