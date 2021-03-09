from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from .forms import *

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = RegistrationForm()
    return render(request, 'sign_up.html', {'form': form})

def login_view(request):

    if request.method == "GET":
        my_form = LoginForm()
        return render(request, 'login.html', {'my_form': my_form})

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')

        else:
            return redirect('login')

def logout_view(request):
    logout(request)
    return redirect ('homepage')

def profile(request, pk):
    my_profile = User.objects.get(id=pk)
    return render(request, 'profile.html', {'my_profile': my_profile})