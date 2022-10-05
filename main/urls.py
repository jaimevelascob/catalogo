from django.urls import path
from main import views


urlpatterns = [
    path('', views.articles, name='articles'),
    path('sign-up', views.signUp, name='sign-up'),
    path('<int:pk>', views.article, name='article'),
    path('aboutus', views.aboutUs, name='aboutus'),
]
