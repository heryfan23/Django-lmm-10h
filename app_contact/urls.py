from django.urls import path
from .views import *
urlpatterns = [
    path("contact/",aff_contact,name="contact")
]
