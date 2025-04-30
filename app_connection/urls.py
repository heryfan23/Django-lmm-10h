from django.urls import path
from .views import *
urlpatterns = [
    path("connection/",aff_connection,name="connection"),
    path("inscription/",aff_inscription,name="inscription"),
    path('inscription',faire_inscription,name="inscription"),
    
    path("connection",faire_connection,name="connecter_membre"),
    path("deconnexion",deconnexion,name="deconnexion"),
]

