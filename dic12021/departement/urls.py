from django.contrib import admin
from django.urls import path , include
from departement import views 
urlpatterns = [
    path('/deptgit',views.git,name='genie_git'),
    

]
