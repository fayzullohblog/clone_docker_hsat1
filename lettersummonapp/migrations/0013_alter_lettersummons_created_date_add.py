# Generated by Django 4.0 on 2024-01-29 05:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lettersummonapp', '0012_alter_lettersummons_created_date_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lettersummons',
            name='created_date_add',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 3, 5, 43, 23, 288794, tzinfo=utc)),
        ),
    ]