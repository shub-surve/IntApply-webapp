# Generated by Django 5.1.3 on 2024-12-09 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_remove_userprofile_educations_education_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='about_me',
            field=models.TextField(blank=True, null=True),
        ),
    ]