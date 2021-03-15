from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

def index_view(request):
    return render(request, 'index.html', {'indexes': Index.objects.all()})

def index_view_pk(request):
    pass

def thread_view(request, pk):

    if request.method == "GET":
        form = CommentForm()
        context = {
            'form': form,
        }
        return render(request, 'thread.html', context)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    
    else:
        form = CommentForm()
        context = {
            'form': form,
        }
        return render(request, 'thread.html', context)
