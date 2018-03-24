# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime

from models import Animal

@require_http_methods(['GET'])
@csrf_exempt
def get_animals(request, owner_id):
    animals = Animal.objects.filter(owner_id=int(owner_id))
    return HttpResponse(animals)


@require_http_methods(['POST'])
@csrf_exempt
def create_animal(request):
    received_data = json.loads(request.body)
    birthday = datetime.datetime.strptime(received_data['birthday'], "%Y-%m-%d").date()
    animal = Animal.objects.create(name=received_data['name'], owner_id=received_data
        ['owner_id'], animal_type=received_data['animal_type'], birthday=birthday)
    return HttpResponse("animal created : " + str(animal))


@require_http_methods(['DELETE'])
@csrf_exempt
def delete_animal(request):
    received_data = json.loads(request.body)
    Animal.objects.filter(id=received_data['animal_id']).delete()
    return HttpResponse("animal deleted")