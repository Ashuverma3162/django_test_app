# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Animal

class AnimalAdmin(admin.ModelAdmin):
    """
    This class ensures that the user can perform CRUD operations only
    on animals created by a user. An admin can perform these operations on all 
    animals.
    """
    def get_queryset(self, request):
        animal_queryset = super(AnimalAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return animal_queryset
        return animal_queryset.filter(owner_id=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()


admin.site.register(Animal, AnimalAdmin)

