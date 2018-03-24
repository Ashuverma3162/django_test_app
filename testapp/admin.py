# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Animal

class AnimalAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(AnimalAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner_id=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()


# Register your models here.
admin.site.register(Animal, AnimalAdmin)

