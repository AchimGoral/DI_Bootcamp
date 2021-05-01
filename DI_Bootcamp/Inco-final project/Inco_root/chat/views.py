from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def room_base_view(request):
    return render(request, 'room_base.html', {})

@login_required
def room_view(request, room_name):
    return render(request, 'room_chat.html', {'room_name': room_name})