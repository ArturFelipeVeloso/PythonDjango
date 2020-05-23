# Generated by Django 3.0.5 on 2020-05-23 18:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_post_categorias'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='alterado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='cadastrado',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='publicado',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 23, 18, 58, 12, 520607, tzinfo=utc)),
        ),
    ]