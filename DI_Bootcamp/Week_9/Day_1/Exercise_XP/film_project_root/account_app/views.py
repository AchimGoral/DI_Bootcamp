from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import *

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            # Stay logged in after signing up
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'],)
            login(request, user)
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
            messages.error(request, 'Username and/or password incorrect. Please try again')
            return redirect('login')

def logout_view(request):
    logout(request)
    return redirect ('homepage')

def profile(request, pk):
    my_profile = User.objects.get(id=pk)
    return render(request, 'profile.html', {'my_profile': my_profile})

def profile_edit(request):
    if request.method == "GET":
        user_form = UserChange()
        return render(request, 'edit_user.html', {'user_form': user_form})

    if request.method == "POST":
        user_form = UserChange(request.POST, instance = request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('homepage')
    
    else:
        user_form = UserChange()
        return render(request, 'edit_user.html', {'user_form': user_form})