# Generated by Django 4.0 on 2024-01-13 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TinyNoSigned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('new_desc', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
