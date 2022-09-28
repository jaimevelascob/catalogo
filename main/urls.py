from django.urls import path
from main import views
from .views import registro


urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('<int:pk>', views.news, name='news'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('subscribe', views.subscribe, name='subscribe'),
<<<<<<< HEAD
    path('registro/', registro, name="registro"),  
=======
    path('article', views.article, name='article'),  
>>>>>>> b86020849197a9e95922316132b5d49c5ae3837d
]
