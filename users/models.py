from calendar import c
from django.contrib.auth.models import AbstractUser
from django.db import models


GENDER_SELECTION = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('NS', 'Not Specified'),
]

class CustomUser(AbstractUser):
    gender = models.CharField(max_length=20, choices=GENDER_SELECTION)
    phone_number = models.CharField(max_length=30)
