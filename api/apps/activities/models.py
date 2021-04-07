from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from apps.account.models import UserProfile


class Comment(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL(), null=True)
    text = models.CharField(max_length=256)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=64, choices=(('public', 'public'), ('private', 'private')))


class Rate(models.Model):
    # content = models.ForeignKey()
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE())
    user = models.ForeignKey(User, on_delete=models.CASCADE())
    date = models.DateTimeField(auto_now_add=True, editable= False)
