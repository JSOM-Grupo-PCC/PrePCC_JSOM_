# Generated by Django 4.2.7 on 2024-02-08 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsom_sga', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='dark_mode',
            field=models.BooleanField(default=False),
        ),
    ]
