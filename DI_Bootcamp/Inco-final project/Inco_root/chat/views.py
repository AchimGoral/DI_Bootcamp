from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def room_view(request, room_name):
    return render(request, 'chatroom.html', {'room_name': room_name})