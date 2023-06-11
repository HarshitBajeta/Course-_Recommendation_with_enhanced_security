from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('my_learning', views.learning, name='my_learning'),
    path('recommend/', views.recommend_ui, name='recommend_ui'),
    path('recommend_books/', views.recommend, name='recommend'),
    # path('face_authentication/', views.face_authentication, name='face_authentication'),
]
