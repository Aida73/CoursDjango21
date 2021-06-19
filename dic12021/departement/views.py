from django.shortcuts import render

# Create your views here.




def git(request):

	context={
		"git" : "Departement GIT",
		"liste_ing":["Aida Sow","demba Dia","abdou ndiaye","doudou mané"],
		"user_connected": True

	}
	return render(request,'git.html',context)