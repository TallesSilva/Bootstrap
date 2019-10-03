from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    return render(request, 'dashboard.html')

def about(request):
    return render(request, 'about.html')

def configure(request):
    return render(request, 'configure.html')

def entrie(request):
    return render(request, 'entrie.html')

def user(request):
    return render(request, 'user.html')

def option(request):
    return render(request, 'option.html')