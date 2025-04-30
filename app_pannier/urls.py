from django.urls import path
from .views import *

urlpatterns = [
    path("pannier/<int:id>",ajout_pannier,name="pannier")
]
