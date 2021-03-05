from django.shortcuts import render
from .models import *
from .forms import *
from django.http import Http404

# Create your views here.
def home(request):
    pass
    todo = Todo()
    category = Category()

def create(request):

    if request.method == "GET":
        try:
            myform = Todoform()
            return render(request, 'create.html', {'myform':myform})
        except:
            return render(request, '404.html')

    if request.method == "POST":

        myform = Todoform(request.POST)

        if myform.is_valid():
            title=myform.cleaned_data['title']
            details=myform.cleaned_data['details']
            has_been_done=myform.cleaned_data['has_been_done']
            deadline_date=myform.cleaned_data['deadline_date']
            
            m1 = Todo(title=title, details=details, has_been_done=has_been_done, deadline_date=deadline_date)
            m1.save()

            return redirect('home.html')

        else:
            return render(request, 'create.html', {'myform':myform})