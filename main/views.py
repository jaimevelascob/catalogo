from django.shortcuts import render, redirect

from main.models import Article, Comments
from main.forms import signUpForm
from main.forms import signInFrom
from django.contrib.auth import login, logout, authenticate


def articles(request):
    article = Article.objects.all()
    comments = Comments.objects.all()

    context = {
        'article': article,
        'comments': comments,

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
            
    return render(request, 'articles.html', context)


def article(request, pk):
	article = Article.objects.get(pk=pk)
	
	context = {
		'article' : article,
        
	}
	return render(request, 'article.html', context)


def signUp(request):

    form = signUpForm()

    if request.method == "POST":
        form = signUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect("/")

    else:      
        return render(request, 'registration/signup.html', {"form" : form})



def aboutUs(request):
    return render(request, 'aboutus.html')