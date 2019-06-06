from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('/index/', views.index),
    path('/login/', views.login),
    path('/register/', views.register),
    path('/logout/', views.logout),
]
