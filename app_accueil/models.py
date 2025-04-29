from django.db import models

# Create your models here.
class Produits(models.Model):
    nom = models.CharField(max_length=150)
    types = models.CharField(max_length=150)
    description = models.TextField()
    prix = models.IntegerField()
    images = models.ImageField(upload_to="static/images/")
    date = models.DateTimeField(auto_now_add=True)

