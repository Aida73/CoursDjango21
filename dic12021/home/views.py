from django.shortcuts import render

# Create your views here.


def accueil(request):
	context={"dic1" : "DIC DE L'EPT"}
	return render(request,'index.html',context)




