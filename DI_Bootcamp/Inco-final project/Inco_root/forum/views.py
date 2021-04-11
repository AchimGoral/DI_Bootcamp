import os
from django.shortcuts import render, redirect, get_object_or_404
from . import urls
from .models import File
from .forms import FileForm
from accounts.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import FileResponse, HttpResponse, HttpResponseNotFound
from django.core.files.storage import FileSystemStorage
from wsgiref.util import FileWrapper

def forum_view(request):
    return render(request, 'forum.html', {'forms': File.objects.all()})

@login_required
def forum_entry_view(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.profile = request.user.profile
            f.save()
            return redirect('forum')
    else:
        form = FileForm()
        return render(request, 'forum_entry.html', {'form': form})

@login_required
def forum_file_view(request, pk):
    obj = File.objects.get(pk=pk)
    file_path = obj.document.path
    file_name = file_path.split("\\")[-1]
    response = FileResponse(open(file_path, 'rb'), content_type='application/force-download')
    response['Content-Disposition'] = f'inline; filename={file_name}'
    return response