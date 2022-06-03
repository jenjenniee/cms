from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Plan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date = models.DateField()