# Generated by Django 3.0.5 on 2020-05-23 19:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20200523_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ativado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='publicado',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 23, 19, 3, 55, 592557, tzinfo=utc)),
        ),
    ]
