from django.db import models

# Create your models here.
class Membres(models.Model):
    nom = models.CharField(max_length=250)
    pseudo = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.TextField()
    password = models.TextField()
    photo = models.ImageField(upload_to="static/images/membres/")
    date = models.DateTimeField()
    
    def __str__(self):
        return self.pseudo

