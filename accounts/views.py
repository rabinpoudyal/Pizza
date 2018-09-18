from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def login(request):
    if request.method == "POST":
        pass
    else:
        return render(request, 'accounts/login.html')

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render(request, 'accounts/signup.html', {"error": "Username already taken"})
            except User.DoesNotExist:
                u = User.objects.create(username=request.POST['username'],email=request.POST['email'],password=request.POST['password1'])
                auth.login(request, u)
                return redirect('root')
    else:
        return render(request, 'accounts/signup.html')

def logout(request):
    return HttpResponse("Logged out")