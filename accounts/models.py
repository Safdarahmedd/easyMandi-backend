from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstName = models.TextField(max_length=50)
    lastName = models.TextField(max_length=50, blank=True, null=True)
    meta = models.CharField(max_length=80)
    district = models.TextField(max_length=60, blank=True, null=True)
    state = models.TextField(max_length=20, blank=True)
    dob = models.DateField(null=True, blank=True)
    MALE = 'Male'
    FEMALE = 'Female'
    P = 'Prefer not to say'
    gender = models.TextField(max_length=20, choices=[(MALE, 'Male'), (FEMALE, 'Female'), (P, 'Prefer not to say')], default=FEMALE)

    def __str__(self):
        return self.user.username