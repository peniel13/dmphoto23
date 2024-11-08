from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.text import slugify # type: ignore

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(upload_to="p_img", blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
    
    def __str__(self):
        return self.email

class Album(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Photo(models.Model):
    album = models.ForeignKey(Album, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Photo in {self.album.title}'
    


class ServiceOrder(models.Model):
    SERVICE_CHOICES = [
        ('mariage', 'Mariage'),
        ('corporate', 'Corporate'),
        ('evenement', 'Événement'),
        ('famille', 'Famille'),
        ('video', 'Vidéo'),
        ('culinaire', 'Culinaire'),
        ('autres', 'Autres'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='service_orders')
    nom = models.CharField(max_length=100)
    postnom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=15)
    date_commande = models.DateField()
    nombre_heures = models.PositiveIntegerField()
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} {self.postnom} - {self.service}"

class LivraisonAlbum(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class LivraisonPhoto(models.Model):
    album = models.ForeignKey(LivraisonAlbum, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='livraison_photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Photo in {self.album.title}'



