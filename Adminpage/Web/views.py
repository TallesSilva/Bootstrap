from django.shortcuts import render
from django.http import HttpResponse

def post_list(request):
    return render(request, 'base/post_list.html')

def about(request):
    return render(request, 'base/about.html')

def contact(request):
    return render(request, 'base/contact.html')