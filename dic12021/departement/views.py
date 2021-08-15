from django.shortcuts import render
from users.views import *
from users.models import *
from departement.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


"""
Pour respecter le principe du DRY, je crée cette fonction  qui permet de récupérer les étudiants de tout niveau d'un département donné
Cette fonction pourra etre utilisé pour chaque département
"""
def liste_etudiants_classe(request,niveau,dept):
	classe = Classe.objects.get(niveau__niveau=niveau, dept__nom_dept=dept)
	etudiants = Etudiant_Classe.objects.filter(classe=classe).order_by('etudiant__user__last_name')
	return etudiants



@login_required(login_url='/#exampleModal2')
def git(request):
	context={
		'etudiants_dic1':liste_etudiants_classe(request,"DIC1","Génie Informatique et Télécoms"),
		'etudiants_dic2':liste_etudiants_classe(request,"DIC2","Génie Informatique et Télécoms"),
		'etudiants_dic3':liste_etudiants_classe(request,"DIC3","Génie Informatique et Télécoms"),
	}
	return render(request,'departement/git.html',context)

def gem(request):
	return render(request,'departement/gem.html')


def gc(request):
	return render(request,'departement/gc.html')



def aero(request):
	return render(request,'departement/aero.html')


def propos(request):
	return render(request,'departement/propos.html')