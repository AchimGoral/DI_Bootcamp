from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def sign_up_view(request):

    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        profile_form = ProfileUpdateForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            # Stay logged in after signing up
            user = authenticate(username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password1'],)
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            messages.success(request, f'{user.username} signed up sucessfully')
            return redirect('profile')

    else:
        user_form = RegistrationForm()
        profile_form = ProfileUpdateForm()
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'signup.html', context)


def login_view(request):

    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')

        else:
            messages.error(request, 'Username and/or password incorrect. Please try again')
            return redirect('login')

@login_required
def logout_view(request):

    logout(request)
    return redirect ('login')

@login_required
def profile_view(request):

    return render(request, 'profile.html')
    
@login_required
def profile_edit(request):

    if request.method == "GET":
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }

        return render(request, 'profile_edit.html', context)

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    
    else:
        user_form = UserUpdateForm()
        profile_form = ProfileUpdateForm()
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'profile_edit.html', context)