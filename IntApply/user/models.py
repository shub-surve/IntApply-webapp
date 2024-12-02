from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField

HIGHEST_EDUCATION_CHOICES = [
        ('HS', 'High School'),
        ('AA', 'Associate Degree'),
        ('BA', 'Bachelor\'s Degree'),
        ('MA', 'Master\'s Degree'),
        ('PHD', 'Doctorate'),
        ('OT', 'Other'),
    ]
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contactNo = models.CharField(max_length=15 , blank=True)
    country = CountryField(blank_label="(Select Country)")
    college_name = models.CharField(max_length=50)
    highest_education = models.CharField(
        max_length=150,
        choices=HIGHEST_EDUCATION_CHOICES,
        default='OT',
    )
    profile_completed = models.BooleanField(default=False)
