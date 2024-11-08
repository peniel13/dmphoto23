
from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=25)
    
    def __str__(self):
        return self.title

class CategoryVideo(models.Model):
    title = models.CharField(max_length=25)
    
    def __str__(self):
        return self.title

class BlogVideo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name="blogs_videos")
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)  # Optionnel, si tu veux ajouter une description textuelle.
    thumbnail = models.ImageField(upload_to="videos/thumbnails/")
    video = models.FileField(upload_to="videos/")  # Le fichier vidéo
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    featured = models.BooleanField(default=False)
    categoryvideo = models.ForeignKey(CategoryVideo, on_delete=models.CASCADE, blank=True, null=True, related_name="videos")
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogVideo, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title


    

class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name="blogs")
    title = models.CharField(max_length=50, unique=True)
    slug=models.SlugField(blank=True, null=True)
    body = models.TextField()
    thumbnail = models.ImageField(upload_to="img")
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="blogs")
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    
    def __str__(self):
        return self.body
    
    
class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
    
class Contact1(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    content = models.TextField(max_length=400)
    number  = models.CharField(max_length=10)

    def __str__(self):
        return (self.name)
    
class Testimonial(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="testimonials", null=True, blank=True)  # Allow null and blank
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.user:
            return f'Témoignage de {self.user.username}'
        return 'Témoignage anonyme' 
    

from django.utils.text import slugify

class BlogMariage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_mariage/', null=True, blank=True, default='default_image.jpg')  # Example with default value
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.title




class BlogPhoto(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='photo_immobilier/', null=True, blank=True)  # Champ image ajouté ici
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class BlogCulinaire(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='photo_culinaire/', null=True, blank=True)  # Champ image ajouté ici
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class BlogFamille(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='photo_famille/', null=True, blank=True)  # Champ image ajouté ici
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Evenement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='photo_evenement/', null=True, blank=True)  # Champ image ajouté ici
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class BlogCorporate(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='photo_corporate/', null=True, blank=True)  # Champ image ajouté ici
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class BlogConference(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='photo_conference/', null=True, blank=True)  # Champ image ajouté ici
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title