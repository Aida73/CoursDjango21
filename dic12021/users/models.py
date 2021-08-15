from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Etudiant (models.Model):
    numero_carte = models.CharField(max_length=50)  
    date_Nce = models.DateField(null=True)
    lieu_naissance  = models.CharField(max_length=200)  
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.numero_carte


class Professeur (models.Model):
    contact_prof = models.CharField(max_length=50)  
    date_d_adhesion  = models.CharField(max_length=200)  
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name










   


