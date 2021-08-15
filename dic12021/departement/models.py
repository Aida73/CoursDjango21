from django.db import models
from django.contrib.auth.models import User
from users.models import *

# Create your models 

class Department(models.Model):
    nom_dept= models.CharField(max_length=200)
    mail_dept=models.EmailField(max_length=254)
    numero_dept=models.CharField(max_length=13)
    description_dept= models.TextField(null=True)


    class Meta:
        verbose_name = ("Department")
        verbose_name_plural = ("Departments")

    def __str__(self):
        return f"{self.nom_dept}"


class Matiere(models.Model):
    """
        Comme on a pas de champs supplémentaires au niveu de la table d'association
        on a pas besoin de la créer, le manyTomany peut gérer ça
    """
    nom_matiere=models.CharField(max_length=200)
    code_matiere = models.CharField( max_length=100)
    coef_matiere = models.FloatField()
    credit_matiere = models.FloatField()
    quota_horaire = models.IntegerField()
    description_matiere = models.TextField()
    prof = models.ManyToManyField(Professeur,related_name="prof_matiere")

    def __str__(self):
        return self.nom_matiere


class Niveau(models.Model):
    niveau = models.CharField(max_length=200)
    description_niveau = models.TextField()


    def __str__(self):
        return self.niveau  


class Classe(models.Model):
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE,default=1)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.niveau} {self.dept}"


  

class UE_matiere(models.Model):
    nom_UE = models.CharField(max_length=200)
    code_UE = models.CharField(max_length=100)
    matieres = models.ManyToManyField(Matiere,related_name="matiere_ue")
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_UE

    def coef_UE(self):
        return sum([matiere.coef_matiere for matiere in self.matieres])

    def credit_UE(self):
        return sum([matiere.credit_matiere for matiere in self.matieres])

    

class ProfDept (models.Model):
    """
    cette classe a été implémenté pour pouvoir connaitre
    le departement dont un professeur est responsable
    """
    prof = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    dept= models.ForeignKey(Department, on_delete=models.CASCADE)
    isChefDept = models.BooleanField(default=False)


    def __str__(self):
        return self.prof

class Etudiant_Classe (models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    annee_scolaire = models.CharField(max_length=200)


    def __str__(self):
        return self.etudiant.user.username

   




