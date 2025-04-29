from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import HttpResponse


# Create your views here.

def signup(request):

    if request.method == "GET":
        return render(request, 'core/signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except:
                return render(request, 'core/signup.html',{
                    'form': UserCreationForm,
                    'error': "User already exists" 
                })
        return render(request, 'core/signup.html', {
            'form': UserCreationForm,
            'error': "Password do not match"
        })

def tasks(request):
    return render(request, 'core/tasks.html')


def home(request):
    return render(request, "core/home.html")

def about_me(request):
    return render(request, "core/about-me.html")


