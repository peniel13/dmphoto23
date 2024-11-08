from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegisterForm, UpdateProfileForm,AlbumForm, PhotoForm,ServiceOrderForm,LivraisonAlbumForm, LivraisonPhotoForm
from django.contrib import messages
from base.forms import TestimonialForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .models import Album, Photo,ServiceOrder,LivraisonAlbum,LivraisonPhoto
from base.models import Testimonial
 


def signup(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Compte creer avec success")
            return redirect("signin")
        
    context = {"form":form}
    return render(request, "core/signup.html", context)

def signin (request):
    if request.method == 'POST':
        email = request.POST["email"]
        password= request.POST["password"]

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    context= {}
    return render(request, "core/login.html", context)

def signout(request):
    logout(request)
    return redirect("index")

@login_required(login_url="signin")
def profile(request):
    user = request.user
    albums = Album.objects.filter(user=user)
    orders = ServiceOrder.objects.filter(user=user)
    livraison_albums = LivraisonAlbum.objects.filter(user=user)

    # Gestion du formulaire d'album
    if request.method == 'POST':
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            album = album_form.save(commit=False)
            album.user = user
            album.save()
            messages.success(request, "Album créé avec succès !")
            return redirect('profile')
    else:
        album_form = AlbumForm()

    # Gestion du formulaire de témoignage
    if request.method == 'POST':
        testimonial_form = TestimonialForm(request.POST)
        if testimonial_form.is_valid():
            testimonial = testimonial_form.save(commit=False)
            testimonial.user = user
            testimonial.save()
            messages.success(request, "Témoignage soumis avec succès !")
            return redirect('profile')
    else:
        testimonial_form = TestimonialForm()

    # Gestion du formulaire de commande de service
    if request.method == 'POST':
        service_order_form = ServiceOrderForm(request.POST)
        if service_order_form.is_valid():
            service_order = service_order_form.save(commit=False)
            service_order.user = user  # Assurez-vous que l'utilisateur est connecté
            service_order.save()
            messages.success(request, "Commande envoyée avec succès !")
            return redirect('profile')  # Reste sur la page du profil
    else:
        service_order_form = ServiceOrderForm()

    context = {
        "user": user,
        "albums": albums,
        "orders": orders,
        "livraison_albums": livraison_albums,
        "album_form": album_form,
        "testimonial_form": testimonial_form,
        "service_order_form": service_order_form,  # Ajouter le formulaire de commande de service au contexte
    }
    return render(request, "core/profile.html", context)



@login_required(login_url="signin")
def update_profile(request):
    if request.user.is_authenticated:
        user = request.user
        form = UpdateProfileForm(instance=user)
        if request.method == 'POST':
            form = UpdateProfileForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile updated successfully")
                return redirect("profile")
                
    context = {"form": form}
    return render(request, "core/update_profile.html", context)


def album_list(request):
    albums = Album.objects.filter(user=request.user)
    return render(request, 'core/album_list.html', {'albums': albums})

def album_detail(request, album_id):
    album = Album.objects.get(id=album_id)
    return render(request, 'core/album_detail.html', {'album': album})

def delete_photo(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    album_id = photo.album.id
    photo.delete()
    return redirect('album_detail', album_id=album_id)

def delete_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    album.delete()
    return redirect('album_list')

@login_required(login_url="signin")
def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            album.save()
            return redirect('profile')  # Redirige vers le profil après la création
    else:
        form = AlbumForm()
    return render(request, 'core/create_album.html', {'form': form})


def upload_photo(request, album_id):
    album = Album.objects.get(id=album_id)
    if request.method == 'POST':
        # Récupérer la liste des fichiers téléchargés
        images = request.FILES.getlist('images')
        
        # Enregistrer chaque image dans la base de données
        for image in images:
            photo = Photo(album=album, image=image)
            photo.save()

        return redirect('album_detail', album_id=album.id)
    else:
        form = PhotoForm()
    
    return render(request, 'core/upload_photo.html', {'form': form, 'album': album})



from django.http import HttpResponse
import zipfile
import os

# Télécharger une photo
def download_photo(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    response = HttpResponse(content_type='image/jpeg')
    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(photo.image.name)}"'
    response.write(photo.image.read())
    return response

# Télécharger un album complet
def download_album(request, album_id):
    album = Album.objects.get(id=album_id)
    zip_filename = f"{album.title}.zip"
    response = HttpResponse(content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename={zip_filename}'

    with zipfile.ZipFile(response, 'w') as zip_file:
        for photo in album.photos.all():
            zip_file.writestr(os.path.basename(photo.image.name), photo.image.read())

    return response


def service_order(request):
    if request.method == 'POST':
        form = ServiceOrderForm(request.POST)
        if form.is_valid():
            service_order = form.save(commit=False)
            service_order.user = request.user  # Assurez-vous que l'utilisateur est connecté
            service_order.save()
            messages.success(request, "Commande envoyée avec succès !")  # Message de succès
            return redirect("index")  # Redirection vers la page souhaitée
    else:
        form = ServiceOrderForm()
    return render(request, 'core/service_order.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import LivraisonAlbum
from .forms import LivraisonAlbumForm, LivraisonPhotoForm

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from .forms import LivraisonAlbumForm
from django.contrib.auth import get_user_model

User = get_user_model()

@user_passes_test(lambda u: u.is_superuser)  # Réservé à l'admin
def create_livraison_album(request):
    if request.method == 'POST':
        album_form = LivraisonAlbumForm(request.POST)
        if album_form.is_valid():
            album = album_form.save()  # Créer l'album
            return redirect('add_photos', album_id=album.id)  # Rediriger vers la vue d'ajout de photos
    else:
        album_form = LivraisonAlbumForm()

    users = User.objects.all()  # Récupérer tous les utilisateurs

    return render(request, 'core/create_livraison_album.html', {
        'album_form': album_form,
        'users': users,
    })




@user_passes_test(lambda u: u.is_superuser)
def add_photos(request, album_id):
    album = get_object_or_404(LivraisonAlbum, id=album_id)
    
    if request.method == 'POST':
        # Récupérer la liste des fichiers téléchargés
        images = request.FILES.getlist('image')  # Assurez-vous que le champ est 'image' dans le formulaire
        
        # Enregistrer chaque image dans la base de données
        for image in images:
            LivraisonPhoto.objects.create(album=album, image=image)
        
        return redirect('livraison_album_detail', album_id=album.id)  # Rediriger vers la vue des détails de l'album

    else:
        photo_form = LivraisonPhotoForm()

    return render(request, 'core/add_photos.html', {
        'photo_form': photo_form,
        'album': album,
    })

def livraison_album_detail(request, album_id):
    album = get_object_or_404(LivraisonAlbum, id=album_id)
    photos = album.photos.all()  # Récupérer toutes les photos associées à cet album

    return render(request, 'core/livraison_album_detail.html', {
        'album': album,
        'photos': photos,
    })

