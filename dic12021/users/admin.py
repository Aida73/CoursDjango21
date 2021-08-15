from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display=('numero_carte','lieu_naissance','date_Nce','user')

@admin.register(Professeur)
class ProfesseurAdmin(admin.ModelAdmin):
    list_display=('contact_prof','user','date_d_adhesion')

    


    

