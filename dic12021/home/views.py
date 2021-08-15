from django.shortcuts import render
from users.forms import MyForm
from departement.models import *
from users.models import *
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
# Create your views here.


def accueil(request):
	depts = Department.objects.all()
	niveaux = Niveau.objects.all()
	form=MyForm()
	context={
		'form':form,
		'depts':depts,
		'niveaux':niveaux
	}
	return render(request,'departement/index.html',context)




def contact(request):
	return render(request,'departement/contact.html')







