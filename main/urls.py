from django.urls import path
from main import views
from .views import signUp


urlpatterns = [
    path('', views.article, name='article'),
    path('signup', views.signUp, name='signup'),
    path('signin', views.signIn, name='signin'),
    path('<int:pk>', views.news, name='news'),

]
