from django.contrib import admin
from django.urls import path , include
from users import views
urlpatterns = [
    path('register',views.register,name='myregister'),
    path('signIN',views.signIn,name='signIN'),
    path('deconnexion',views.myLogout, name='mylogout'),

]