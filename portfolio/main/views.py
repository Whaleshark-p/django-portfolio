from django.shortcuts import render
from .models import Project

# Create your views here.

def home(response):
    return render(response, "main/home.html", {})

def projecten(response):
    y = 0
    for x in Project.objects.all():
        y = y + 1
    return render(response, "main/projecten.html", {"smallw":y//2, "largew":y//3, "projects": Project.objects.all().order_by('id').reverse()})

def cv(response):
    return render(response, "home/cv.html", {})