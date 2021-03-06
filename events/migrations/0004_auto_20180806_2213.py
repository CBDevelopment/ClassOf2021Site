# Generated by Django 2.0.7 on 2018-08-07 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(help_text='Pick the date with the calendar icon'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(help_text='Use military time i.e. 6p.m. is 18:00'),
        ),
        migrations.AlterField(
            model_name='event',
            name='pub_date',
            field=models.DateTimeField(help_text="Click 'Today' and 'Now'", verbose_name='Publication date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(help_text='Use military time i.e. 3p.m. is 15:00'),
        ),
    ]
