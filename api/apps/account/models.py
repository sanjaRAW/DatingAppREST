from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    genders = (
        ("M", "M"),
        ("W", "W"),
        ("other", "other"),
    )
    full_name = models.CharField(max_length=64)
    date_birth = models.DateField()
    gender = models.CharField(max_length=32, choices=genders)
    bio = models.TextField()
    photo = models.ImageField()
    user = models.OneToOneField(User, on_delete=models.SET_NULL(), null=True)

class Hobby(models.Model):
    name = models.CharField(max_length=64)
    text = models.TextField()
    userprofile = models.ForeignKey(UserProfile, on_delete= models.CASCADE())

