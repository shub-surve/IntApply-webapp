# Generated by Django 5.1.3 on 2024-12-02 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_completed',
            field=models.BooleanField(default=False),
        ),
    ]
