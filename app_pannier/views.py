from django.shortcuts import render,redirect
from app_accueil.models import Produits
# Create your views here.
def ajout_pannier(request,id):
    prod = Produits.objects.get(pk=id)
    
    if "cart" not in request.session:
        request.session['cart'] = []
        
    cart = request.session['cart']
    
    obj= {
        "id_prod":int(prod.id),
        "type":prod.types,
        "nom": prod.nom,
        "prix" : prod.prix,
        "image" : str(prod.images),
        "desc" : prod.description,
        "nombre": len(cart)
    }
    if obj not in cart:
        cart.append(obj)
        request.session["nombre_pannier"] = len(cart)
        request.session.modified = True
    
    return redirect(f"http://127.0.0.1:8000/aff_details/{prod.id}")