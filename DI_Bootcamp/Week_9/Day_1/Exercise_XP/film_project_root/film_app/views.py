from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
def homepage(request):
    films = Film.objects.all()
    context = {
        'films':films,
    }
    return render(request, 'homepage.html', context)

def homepage_detail(request):
    pass

def add_film(request):
    if request.method == "GET":
        return render(request, 'add_film.html', {'film':AddFilmForm()})

    if request.method == 'POST':

        film = AddFilmForm(request.POST)

        if film.is_valid():
            film.save()
            messages.success(request, 'The film was succesfully added')
            return redirect('addfilm')

        else:
            messages.error(request, 'Something went wrong. Please try again')
            return render(request, 'add_film.html', {'film':film})


def add_director(request):
    if request.method == "GET":
        return render(request, 'add_director.html', {'director':AddDirectorForm()})

    if request.method == 'POST':

        director = AddDirectorForm(request.POST)

        if director.is_valid():
            director.save()
            messages.success(request, 'The director was succesfully added')
            return redirect('adddirector')

        else:
            messages.error(request, 'Something went wrong. Please try again')
            return render(request, 'add_director.html', {'director':director})

def like(request):
    pass
    