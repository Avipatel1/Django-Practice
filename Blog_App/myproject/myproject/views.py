# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Welcome to the Homepage!")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("About Us")
    return render(request, 'about.html')