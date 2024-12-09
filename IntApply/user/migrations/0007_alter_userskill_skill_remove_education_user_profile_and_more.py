# Generated by Django 5.1.3 on 2024-12-09 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_education_endyear_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userskill',
            name='skill',
            field=models.CharField(max_length=100),
        ),
        migrations.RemoveField(
            model_name='education',
            name='user_profile',
        ),
        migrations.RemoveField(
            model_name='userskill',
            name='user_profile',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='educations',
            field=models.ManyToManyField(blank=True, to='user.education'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skills',
            field=models.ManyToManyField(blank=True, to='user.userskill'),
        ),
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='education',
            name='field_of_study',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='education',
            name='institution_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='userskill',
            name='proficiency_level',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]
