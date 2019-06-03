from . import views
from django.urls import path

urlpatterns = [
    path('', views.polls, name='polls'),
    path('<int:question_id>/', views.detail),
    path('<int:question_id>/results/', views.results),
    path('<int:question_id>/vote/', views.vote),
]