from django.http import HttpResponse
from django.shortcuts import render, redirect

def Home(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def LogOut(request):
    return redirect(request, 'login.html')

def Register(request):
    return render(request, "register.html")

def Login(request):
    return render(request, "login.html")