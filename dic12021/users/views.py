from django.shortcuts import render,redirect
from .models import *
from departement.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def get_date_naissance(mois,jour,annee):
    date = f"{annee}-{mois}-{jour}"
    return date

    
def register(request):
 
    if request.method == "POST":
        prenom = request.POST['prenom']
        nom = request.POST['nom']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        carte = request.POST['carte']
        mois = request.POST['mois']
        jour = request.POST['jour']
        annee = request.POST['annee']
        lieu_naissance = request.POST['lieu_nce']
        annee_scolaire = request.POST['annee_scolaire']
        id_departement = request.POST['departement']
        id_niveau = request.POST['niveau']
       
     
        user = User()
        etudiant = Etudiant()
        niveau = Niveau.objects.get(pk=id_niveau)
        departement = Department.objects.get(pk=id_departement)
        classe_etudiant = Etudiant_Classe()
        classe = Classe.objects.get(dept=departement,niveau=niveau)

       

        user.first_name = prenom
        user.last_name = nom
        user.username = username
        user.email = email
        user.set_password(password)
        user.save()
        login(request,user)

        etudiant.numero_carte = carte 
        etudiant.date_Nce = get_date_naissance(mois,jour,annee)
        etudiant.lieu_naissance = lieu_naissance
        etudiant.user = user
        etudiant.save()
       
        classe_etudiant.annee_scolaire = annee_scolaire
        classe_etudiant.classe = classe
        classe_etudiant.etudiant = etudiant
        classe_etudiant.save() 

        messages.success(request,f"Bienvenu.e {username}. Votre compte a été créé avec succès")
        return redirect('home')


def signIn(request):
    next_ = request.POST['nextt']
    if request.method == "POST":
        username  = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            if next_ != "":
                return redirect(next_)
            return redirect('home')
        else:
            messages.error(request,"Le mot de passe et le nom d'utilisateur ne correspondent pas")
    return render(request,'departement/index.html')
    



def myLogout(request):
    logout(request)
    return redirect('home')