from django.db import models
from django.forms import Form
from django import forms
from django.contrib.auth.models import User


# Create your models here.
class Evaluation(models.Model):
    performance = models.IntegerField()
    potential = models.IntegerField()
    feedback = models.TextField()
    user = models.ForeignKey(User)



