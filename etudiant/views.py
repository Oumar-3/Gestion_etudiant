from django.shortcuts import render,redirect, get_object_or_404
from .forms import EtudiantForm  # Formulaire à créer
from	.models	import	Etudiant	
def	etudiants(request):	
    etudiants	=	Etudiant.objects.all().order_by('-created_at')	

    return	render(request,	'etudiant/etudiants.html',	{'etudiants':	etudiants})
# Create your views here.

def index(request):
    return render(request ,'etudiant/index.html', {'index': index} )

def blog(request):
    return render(request ,'etudiant/blog.html', {'blog': blog} )



# Lire (Read)
def liste_etudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'etudiant/etudiants.html', {'etudiants': etudiants})

# Créer (Create)
def ajouter_etudiant(request):
    if request.method == "POST":
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('etudiants')
    else:
        form = EtudiantForm()
    return render(request, 'etudiant/ajouter_etudiant.html', {'form': form})

# Modifier (Update)
def modifier_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)
    if request.method == "POST":
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('etudiants')
    else:
        form = EtudiantForm(instance=etudiant)
    return render(request, 'etudiant/modifier_etudiant.html', {'form': form})

# Supprimer (Delete)
def supprimer_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)
    if request.method == "POST":
        etudiant.delete()
        return redirect('etudiants')
    return render(request, 'etudiant/supprimer_etudiant.html', {'etudiant':etudiant})
