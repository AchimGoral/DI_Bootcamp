from django.shortcuts import render
from .models import * # Gif(mtm), Category


def main(request):
    gifs = Gif.objects.all()
    context = {'gifs': gifs}
    return render(request, 'main.html', context)

def gif_show(request, gif_id):
    gifs = Gif.objects.get(id=gif_id)
    context = {'gifs': gifs}
    return render(request, 'gif_show.html', context)

def categories(request):
    pass
    # cat = Categories.objects.all()
    # context = {'category': cat}
    # return render(request, 'categories.html', context)