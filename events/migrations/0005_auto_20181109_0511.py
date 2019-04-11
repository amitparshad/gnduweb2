# Generated by Django 2.0.6 on 2018-11-09 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20180701_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('detail', models.TextField()),
                ('image', models.FileField(blank=True, null=True, upload_to='static/events/images')),
                ('department_name', models.CharField(max_length=70)),
                ('semester', models.CharField(max_length=50)),
                ('name_of_announcer', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
