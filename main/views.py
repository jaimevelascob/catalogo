from django.http import HttpResponse
from django.shortcuts import render

from main.models import User, Article, Comments


def main(request):
    return render(request, 'main.html')
    

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

def article(request):
	article = Article.objects.all()
	context = {
		'article' : article,
	}
	return render(request, 'article.html', context)
	