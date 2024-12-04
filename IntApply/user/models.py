from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField
from  django.utils import timezone

HIGHEST_EDUCATION_CHOICES = [
        ('X', 'Class X'),
        ('XII', 'Class XII'),
        ('AA', 'Associate Degree'),
        ('BA', 'Bachelor\'s Degree'),
        ('MA', 'Master\'s Degree'),
        ('PHD', 'Doctorate'),
        ('OT', 'Other'),
    ]
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contactNo = models.CharField(max_length=15, blank=True)
    country = CountryField(blank_label="(Select Country)")
    profilepic = models.ImageField(upload_to='user/profile_pics', blank=True)
    profile_completed = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], blank=True)
    bio = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ProfilePageDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    desc = models.TextField(max_length=1000, default="")
    skills = models.ManyToManyField(Skill, blank=True)
    profile_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s Profile Details"


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='educations')
    highest_education = models.CharField(
        max_length=150,
        choices=HIGHEST_EDUCATION_CHOICES,
        default='OT',
    )
    name = models.CharField(max_length=50)
    startyear = models.PositiveIntegerField()
    endyear = models.PositiveIntegerField()


    def __str__(self):
        return f"{self.name} ({self.startyear} - {self.endyear})"


class UserSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    proficiency_level = models.CharField(max_length=50, choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')])

    def __str__(self):
        return f"{self.user.username} - {self.skill.name} ({self.proficiency_level})"