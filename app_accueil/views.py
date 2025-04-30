from django.shortcuts import render
from .models import Produits
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def aff_accueil(request):
    prod = Produits.objects.all()
    pagination = Paginator(prod,3)

    num_page = request.GET.get('page',1)
    try:
        page = pagination.page(num_page)
    except:
        page = pagination.page(1)


    context = {
        "produits" : prod,
        "listes_prod": page
    }

    return render(request,"index.html",context)

def aff_produits(request):
    tous_produits = Produits.objects.all()

    
    mot_rechercher = request.GET.get('rechercher', '').strip()

    prod_rech = []
    if mot_rechercher:
        prod_rech = Produits.objects.filter(
            Q(nom__icontains=mot_rechercher) | Q(description__icontains = mot_rechercher))

    context = {
        "produits" : tous_produits,
        "prod_rechercher" : mot_rechercher,
        "valeur_rech" : prod_rech
    }

    return render(request,"tous_produits.html",context)

def afficher_details(request,id):
    produits = Produits.objects.get(id=id)
    
    context = {
        "prod" : produits
    }
    return render(request,"detail.html",context)
    