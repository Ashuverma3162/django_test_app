# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Animal(models.Model):
    animal_type = models.CharField(max_length=16, choices=[('dog', 'Dog'), ('cat', 'Cat')])
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)

    def __unicode__(self):
       return self.name

