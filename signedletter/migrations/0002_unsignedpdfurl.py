# Generated by Django 4.0 on 2024-01-22 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signedletter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnSignedPdfurl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('pdf_url', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
