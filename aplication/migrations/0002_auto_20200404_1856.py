# Generated by Django 2.2.8 on 2020-04-04 21:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='app_date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 4, 21, 56, 49, 459412, tzinfo=utc), verbose_name='TimeStamp'),
        ),
    ]
