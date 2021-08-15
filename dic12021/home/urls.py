from django.contrib import admin
from django.urls import path , include
from home import views
urlpatterns = [
    path('',views.accueil,name='home'),
    path('contact',views.contact,name='ourContact'),
]

