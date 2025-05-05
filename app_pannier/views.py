from collections import defaultdict
from django.shortcuts import render, redirect
from app_accueil.models import Produits

# Create your views here.
def ajout_pannier(request, id):
    prod = Produits.objects.get(pk=id)
    
    if "cart" not in request.session:
        request.session['cart'] = []
        
    cart = request.session['cart']
    
    obj = {
        "id_prod": int(prod.id),
        "type": prod.types,
        "nom": prod.nom,
        "prix": prod.prix,
        "image": str(prod.images),
        "desc": prod.description,
        "nombre": len(cart)
    }
    if obj not in cart:
        cart.append(obj)
        request.session["nombre_pannier"] = len(cart)
        request.session.modified = True
    
    return redirect(f"http://127.0.0.1:8000/aff_details/{prod.id}")

def aff_pannier(request):
    cart = request.session.get('cart', [])
    produits_dict = {}

    for prod in cart:
        pid = prod["id_prod"]
        if pid not in produits_dict:
            produits_dict[pid] = prod.copy()
            produits_dict[pid]["nombre"] = 1
        else:
            produits_dict[pid]["nombre"] += 1

    produits_listes = list(produits_dict.values())

    return render(request, "pannier.html", {"produits_tous": produits_listes})

def supprimer_pannier(request,id):
    if 'cart' in request.session:
        cart = request.session["cart"]
        
        for index,valeur in enumerate(cart):
            if valeur["id_prod"] == id:
                del cart[index]
                request.session["nombre_pannier"] -= 1
                break
        request.session["cart"] = cart
        
    return redirect("http://127.0.0.1:8000/mon_pannier/")

def procedure_payement(request):
    return render(request,"procedure.html")