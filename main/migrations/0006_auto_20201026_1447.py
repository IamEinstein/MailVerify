# Generated by Django 3.1.2 on 2020-10-26 09:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20201026_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='id',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 26, 9, 17, 18, 680470, tzinfo=utc)),
        ),
    ]