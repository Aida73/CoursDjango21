from django.contrib import admin
from django.urls import path , include
from departement import views
from .api import getListeClasse, LoginView, myLoginAPI,myLoginAPI2
from knox import views as knox_views

urlpatterns = [
    path('deptgit/',views.git,name='genie_git'),
    path('deptgem/',views.gem,name='genie_gem'),
    path('deptgc/',views.gc,name='genie_gc'),
    path('deptaero/',views.aero,name='genie_aero'),
    path('apropos/',views.propos,name='propos'),
    path('liste_etudiants/<str:niveau>/<str:departement>/<str:annee>',getListeClasse),
    path('login', LoginView.as_view()),
    path('login-api', myLoginAPI, name="loginAPI"),
    path('login-api2', myLoginAPI2, name="loginAPI2"),
    path('logout', knox_views.LogoutAllView.as_view())

]
