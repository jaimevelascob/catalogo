from django.http import HttpResponse
from django.shortcuts import render

from main.models import User, Article, Comments
from main.forms import signUpForm


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
    comments = Comments.objects.all()
    form = signUpForm()

    context = {
        'article': article,
        'comments': comments,
        'form': form,

    }

    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            new_comment = Comments(
                article_id = form.cleaned_data['name'],
                user = form.cleaned_data['username'],
                comment = form.cleaned_data['password'],
            )

            new_comment.save()
            
    return render(request, 'article.html', context)
