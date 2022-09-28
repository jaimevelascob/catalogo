from django.urls import path
from main import views


urlpatterns = [
    path('', views.main, name='main'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('<int:pk>', views.news, name='news'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('article', views.article, name='article'),  
]
