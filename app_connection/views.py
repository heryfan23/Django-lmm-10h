import os
from django.shortcuts import render
from .models import Membres
from datetime import datetime
import hashlib
from django.contrib.auth.hashers import check_password

# Create your views here.
def crypter(password):
    mdp = hashlib.sha256()
    mdp.update(password.encode("utf-8"))
    return mdp.hexdigest()

def entrer_image(request,image):
    if "profile_image" in request.FILES:
        fichiers = request.FILES["profile_image"]
        path = os.path.splitext(fichiers.name)
        
        new_name = f'{image}{path[1]}'
        emplacement = os.path.join("static/images/membres/",new_name)
        
        with open(emplacement,"wb") as destination:
            for donner in fichiers.chunks():
                destination.write(donner)
                
        return new_name
        
    
def aff_connection(request):
    return render(request,"connection.html")

def aff_inscription(request):
    return render(request,"inscription.html")


def faire_inscription(request):
    if request.method == "POST":
        nom = request.POST.get("username")
        pseudo = request.POST.get("pseudo")
        mail = request.POST.get("email")
        contact = request.POST.get("contact")
        password = request.POST.get("password")
        conf_pass = request.POST.get("confirm_password")
        if nom != "" and pseudo != "" and mail != "" and contact != "":
            if password == conf_pass:
                # email_exist = Membres.objects.get(email=email)
                if not Membres.objects.filter(email=mail).exists():
                    Membres.objects.create(
                        nom = nom,
                        pseudo = pseudo,
                        email = mail,
                        contact = contact,
                        password = crypter(password),
                        photo = f"static/images/membres/{entrer_image(request,pseudo)}",
                        date = datetime.now()
                    )
                    return render(request,"connection.html")
                    
                
                else:
                    erreur = "Email existe deja"
                    return render(request,"inscription.html",{"erreur":erreur})

            else:
                erreur = "Mot de passe doit etre identique"
                return render(request,"inscription.html",{"erreur":erreur})
            
        else:
            erreur = "Veuillez remplir tous les champs"
            return render(request,"inscription.html",{"erreur":erreur})
    return render(request,"inscription.html")
        


def faire_connection(request):
    if request.method == "POST":
        mail = request.POST.get("email")
        password = request.POST.get("password")
        
        if mail and password:
            try:
                membre = Membres.objects.get(email=mail)
                if crypter(password) == membre.password:
                    request.session["client"] = {
                        "id" : membre.id,
                        "nom" : membre.nom,
                        "pseudo": membre.pseudo,
                        "images" :str(membre.photo)
                    }
                    return render(request,"index.html")
                else:
                    erreur = "mot de passe ou email non existant"
                    return render(request,"connection.html",{"erreur":erreur})

            except ValueError:
                erreur = "utilisateurs non inscrit"
                return render(request,"connection.html",{"erreur":erreur})
                 
        else:
            erreur = "veuiller remplir tous les champs"
            return render(request,"connection.html",{"erreur":erreur})