from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('usertable/', views.UserTable),
    path('adduser/', views.AddUser),
    path('deleteuser/', views.DeleteBook),
    path('changeuser/', views.ChangeUser),
    path('booktable/', views.BookTable),
    path('addbook/', views.AddBook),
    path('deletebook/', views.DeleteBook),
    path('changebook/', views.ChangeBook),
    path('borrowrecordtable/', views.BorrowRecordTable),
    path('addborrowrecord/', views.AddBorrowRecord),
    path('deleteborrowrecord/', views.DeleteBorrowRecord),
    path('changeborrowrecord/', views.ChangeBorrowRecord),
]
