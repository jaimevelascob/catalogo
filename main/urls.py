from django.urls import path
from main import views
from .views import signUp


urlpatterns = [
    path('', views.main, name='main'),
    path('signup', views.signUp, name='signup'),
    path('signin', views.signIn, name='signin'),
    path('<int:pk>', views.news, name='news'),
    path('aboutus', views.aboutUs, name='aboutus'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('article', views.article, name='article'),  
]
