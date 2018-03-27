# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
from json import dumps

# Create your models here.
class Animal(models.Model):
    """
    A common model has been taken for animal and types are assigned such as
    'Cat' and 'Dog'. This would help in adding more types in future and manage 
    each type efficiently.
    """
    animal_type = models.CharField(max_length=16, choices=[('dog', 'Dog'), ('cat', 'Cat')])
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)

    def __unicode__(self):
       return self.name

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "birthday": dumps(self.birthday, default=json_serial)
        }


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))
