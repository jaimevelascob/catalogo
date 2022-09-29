from django.http import HttpResponse
from django.shortcuts import render

from main.models import User, Article, Comments
from main.forms import signUpForm


def main(request):
    return render(request, 'main.html')


def signin(request):
    return HttpResponse("Hola soy Signin")


def aboutus(request):
    return HttpResponse("Hola soy Aboutus")


def subscribe(request):
    return HttpResponse("Hola soy Subscribe")


def news(request, pk):
	article = Article.objects.get(pk=pk)
	
	context = {
		'article' : article,
        
	}
	return render(request, 'new.html', context)


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

def signup(request):

    form = signUpForm()

    if request.method == "POST":
        form = signUpForm(request.POST)
        if form.is_valid():
            new_signUp = signUp()(
                name=form.cleaned_data["name"],
                Username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )

            new_signUp.save()

    return render(request, 'signup.html')
