from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=('nom_dept','numero_dept')


@admin.register(Matiere)
class MatiereAdmin(admin.ModelAdmin):
    list_display=('nom_matiere',)


@admin.register(Niveau)
class NiveauAdmin(admin.ModelAdmin):
    list_display=('niveau',)


@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    list_display=('niveau','dept')
    


@admin.register(UE_matiere)
class UEmatiereAdmin(admin.ModelAdmin):
    list_display=('nom_UE',)


@admin.register(ProfDept)
class ProfDeptAdmin(admin.ModelAdmin):
    list_display=('prof','dept','isChefDept')

@admin.register(Etudiant_Classe)
class Classe_EtudiantAdmin(admin.ModelAdmin):
    list_display=('etudiant','classe','annee_scolaire')
    

    


    

    

    


    

