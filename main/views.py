from django.http import HttpResponse
from django.shortcuts import render

from main.models import User, Article, Comments


def index(request):
    return HttpResponse("Hola soy Index")

def signup(request):
    return HttpResponse("Hola soy Signup")

def signin(request):
    return HttpResponse("Hola soy Signin")

def aboutus(request):
    return HttpResponse("Hola soy Aboutus")

def subscribe(request):
    return HttpResponse("Hola soy Subscribe")

def news(request):
    return HttpResponse("Hola soy News")
