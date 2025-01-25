from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('myPost/', views.myPost, name='myPost'),
    path('newPost/', views.newPost, name='newPost'),
    path('signout/', views.signOut, name='signout'),
]
