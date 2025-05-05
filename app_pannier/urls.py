from django.urls import path
from .views import *

urlpatterns = [
    path("pannier/<int:id>",ajout_pannier,name="pannier"),
    path("mon_pannier/",aff_pannier,name="mon_pannier"),
    path("suppr/<int:id>",supprimer_pannier,name="suppr"),
    path("procedure_stripe/",procedure_payement,name="procedure_payement"),
    
]
