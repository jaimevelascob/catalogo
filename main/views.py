from django.http import HttpResponse
from django.shortcuts import render

from main.models import User, Article, Comments


def index(request):
	articles = Article.objects.all()
	context = {
		'articles' : articles,
	}
	return render(request, '', context)