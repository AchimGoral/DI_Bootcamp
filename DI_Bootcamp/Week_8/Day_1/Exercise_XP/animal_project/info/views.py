from django.shortcuts import render
from django.http import HttpResponse
import json

def get_animals_data():
    with open('animal.json') as f:
        data = json.load(f)
    return data

def family(request, families_id):
    data = get_animals_data()
    family_list = data['animals']
    context = {}

    context['animals'] = []
    for my_animal in family_list:
        if my_animal['id'] == families_id:
            context['animals'].append(my_animal)

    html = render(request, 'family.html', context)
    return html

def animal(request, animals_id):
    data = get_animals_data()
    animal_list = data['animals']
    context = {}

    for list_item in animal_list:
        if animals_id == list_item['id']:
            context['name'] = list_item['name']

    context['animals'] = []
    for animals in data['animals']:
        if animals['family'] == animals_id:
            context['animals'].append(animals)

    html = render(request, 'animal.html', context)
    return html
