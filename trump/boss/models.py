from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    salary = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return f"username: {self.username}, salary: {self.salary}, year: {self.year}"

