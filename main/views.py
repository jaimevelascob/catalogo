from django.http import HttpResponse
from django.shortcuts import render

from main.models import User, Rols, Article, Comments
from main.forms import signUpForm

def articles(request):
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
            
    return render(request, 'articles.html', context)


def article(request, pk):
	article = Article.objects.get(pk=pk)
	
	context = {
		'article' : article,
        
	}
	return render(request, 'article.html', context)


def signUp(request):

    form = signUpForm()

    context = {
        'form': form, 
    }

    if request.method == "POST":
        form = signUpForm(request.POST)
        if form.is_valid():
            new_signUp = User(
                name=form.cleaned_data["name"],
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
                rol_id = Rols("1")
            )
            
            new_signUp.save()

    return render(request, 'signup.html', context)


def signIn(request):
    return HttpResponse("Hola soy Signin")


def aboutUs(request):
    return render(request, 'aboutus.html')