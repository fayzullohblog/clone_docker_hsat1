# Generated by Django 4.0 on 2024-01-22 07:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lettersummonapp', '0010_alter_lettersummons_created_date_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lettersummons',
            name='created_date_add',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 27, 7, 54, 1, 946906, tzinfo=utc)),
        ),
    ]
