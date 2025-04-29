from django.contrib import admin
from .models import Produits
# Register your models here.
class Ajouts_produits(admin.ModelAdmin):
    list_display = ("nom","types","description","images","date")

admin.site.register(Produits,Ajouts_produits)