from django.urls import path
from .views import *

urlpatterns = [
    path('',aff_accueil,name="page_home"),
    path('aff_tous/',aff_produits,name="tous_produits"),
    path('aff_details/<int:id>',afficher_details,name="detail")
]
