from django.urls import path
from main import views
from .views import signUp


urlpatterns = [
    path('', views.articles, name='articles'),
    path('signup', views.signUp, name='signup'),
    path('signin', views.signIn, name='signin'),
    path('<int:pk>', views.article, name='article'),
    path('aboutus', views.aboutUs, name='aboutus'),
]
