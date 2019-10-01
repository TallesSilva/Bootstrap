from django.shortcuts import render
from django.http import HttpResponse

def post_list(request):
    return render(request, 'post_list.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')