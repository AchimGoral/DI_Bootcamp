from django.shortcuts import render
from django.http import HttpResponse
import json

with open('animal.json') as f:
    data = json.load(f)

def family(request, families_id):
    pass

def animal(request, animals_id):
    family_list = data['animals']
    context = {}

    for list_item in family_list:
        if animals_id == list_item['id']:
            context['name'] = list_item['name']

    context['animals'] = []
    for fam_animal in data['animals']:
        if fam_animal['family'] == animals_id:
            context['animals'].append(fam_animal)

    html = render(request, 'animal.html', context)
    return html
