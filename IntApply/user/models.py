from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilepic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    contactNo = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=1,
        choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')],
        blank=True,
        null=True
    )
    bio = models.TextField(blank=True, null=True)
    profile_completed = models.BooleanField(default=False)
    skills = models.ManyToManyField('UserSkill', blank=True)
    about_me = models.TextField(blank=True , null=True)

    def __str__(self):
        return self.user.username
    
    def calculate_percent(self):
        fields = [self.profilepic , self.contactNo , self.country , self.date_of_birth , self.gender , self.bio , self.about_me]
        sum_fields = sum(1 for field in fields if field)
        total = len(fields)
        return (sum_fields / total) * 100


class Education(models.Model):
    user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE , blank=True , null=True)
    institution_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField(blank=True , null= True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} at {self.institution_name}"


class UserSkill(models.Model):
    skill = models.CharField(max_length=100)
    proficiency_level = models.CharField(max_length=50)

    def __str__(self):
        return self.skill
