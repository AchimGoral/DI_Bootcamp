from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    # Pretend the data came from the db
    missions = [
        "ISS Resulply mission - 04.03.2021",
        "Hubble - 20.12.2021",
        "Get drunk in space - All time"
    ]

    context = {
        "all_missions": missions,
        "director": "Paul Tomkins"
    }

    html_page = render(request, 'home.html', context)
    return html_page