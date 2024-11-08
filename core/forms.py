from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Album, Photo,ServiceOrder,LivraisonAlbum,LivraisonPhoto

class RegisterForm(UserCreationForm):
    email= forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder":"Enter email adress"}))
    username= forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Enter username"}))
    password1= forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder":"Enter password"}))
    password2= forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder":"confirm password"}))
    class Meta:
        model = get_user_model()
        fields = ["email","username","password1","password2"]

class UpdateProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter firstname"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter lastname"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter username"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder": "Enter email address"}))
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control", "placeholder": "Upload image"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter address"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter phone"}))
    bio = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder": "Enter bio"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter phone"}))
    role = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter role"}))
    class Meta:
        model= get_user_model()
        fields= ["first_name", "last_name", "username", "email", "address", "bio", "phone", "role", "profile_pic"]

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input border rounded-lg py-2 px-3 w-full',
                'placeholder': 'Titre de l\'album'
            }),
        }

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']


class ServiceOrderForm(forms.ModelForm):
    class Meta:
        model = ServiceOrder
        fields = ['nom', 'postnom', 'email', 'telephone', 'date_commande', 'nombre_heures', 'service', 'description']
        widgets = {
            'date_commande': forms.DateInput(attrs={'type': 'date', 'class': 'mt-1 p-2 w-full border border-gray-300 rounded-lg'}),
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'mt-1 p-2 w-full border border-gray-300 rounded-lg'}),
            'nom': forms.TextInput(attrs={'class': 'mt-1 p-2 w-full border border-gray-300 rounded-lg'}),
            'postnom': forms.TextInput(attrs={'class': 'mt-1 p-2 w-full border border-gray-300 rounded-lg'}),
            'email': forms.EmailInput(attrs={'class': 'mt-1 p-2 w-full border border-gray-300 rounded-lg'}),
            'telephone': forms.TextInput(attrs={'class': 'mt-1 p-2 w-full border border-gray-300 rounded-lg'}),
            'nombre_heures': forms.NumberInput(attrs={'class': 'mt-1 p-2 w-full border border-gray-300 rounded-lg'}),
            'service': forms.Select(attrs={'class': 'mt-1 p-2 w-full border border-gray-300 rounded-lg'}),
        }




from django.contrib.auth import get_user_model

User = get_user_model()

class LivraisonAlbumForm(forms.ModelForm):
    class Meta:
        model = LivraisonAlbum
        fields = ['title', 'user']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input border rounded-lg py-2 px-3 w-full',
                'placeholder': 'Titre de l\'album de livraison'
            }),
            'user': forms.Select(attrs={
                'class': 'form-input border rounded-lg py-2 px-3 w-full',
            }),
        }

class LivraisonPhotoForm(forms.ModelForm): 
    class Meta:
        model = LivraisonPhoto
        fields = ['image']
       