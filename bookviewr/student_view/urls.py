from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/',views.admin_signup, name="sign_Up"), # this end point is used to register admin from the front end.
    path('book_list/',views.student_view, name="book_list"), # returns a list of books which are in the db.
]