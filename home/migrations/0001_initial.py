# Generated by Django 2.0.7 on 2018-07-30 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body_text', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Announcement',
            },
        ),
    ]
