# forms.py
from django import forms
from .models import Contact,Blog, Category, Comment,Testimonial,Contact1,BlogVideo,BlogCorporate,BlogPhoto

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']
       
class Contact1Form(forms.ModelForm):
    class Meta:
        model = Contact1
        fields = ['name', 'email', 'content', 'number']


class CreateBlogForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Enter title"}))
    body = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder":"Enter body"}))
    thumbnail = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control", "placeholder":"Add image"}))
    # category = forms.CharField(widget=forms.TextInput(attrs={"class": "form-select", "placeholder":"Enter title"}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={"class": "form-select", "placeholder": "Select category"}))
    class Meta:
        model=Blog 
        fields = ["title", "body", "thumbnail", "category"]
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['content']  # On garde seulement le champ content
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }

class BlogVideoForm(forms.ModelForm):
    class Meta:
        model = BlogVideo
        fields = ['title', 'slug', 'thumbnail', 'video', 'categoryvideo', 'featured', 'body']

    # Optionnel: tu peux ajouter une validation supplémentaire pour le fichier vidéo si nécessaire
    def clean_video(self):
        video = self.cleaned_data.get('video')
        if video and not video.name.endswith('.mp4'):
            raise forms.ValidationError("Seul le format vidéo MP4 est autorisé.")
        return video

from .models import BlogMariage

class BlogMariageForm(forms.ModelForm):
    class Meta:
        model = BlogMariage
        fields = ['title', 'description', 'image', 'slug']

        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    # Si vous souhaitez ajouter des validations supplémentaires ou des champs personnalisés, vous pouvez les ajouter ici
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("Le titre est requis.")
        return title

class BlogPhotoForm(forms.ModelForm):
    class Meta:
        model = BlogPhoto
        fields = ['title', 'description', 'image', 'slug']

from .models import BlogCulinaire

class BlogCulinaireForm(forms.ModelForm):
    class Meta:
        model = BlogCulinaire
        fields = ['title', 'description', 'image', 'slug']

from .models import BlogFamille

class BlogFamilleForm(forms.ModelForm):
    class Meta:
        model = BlogFamille
        fields = ['title', 'description', 'image', 'slug']

from .models import Evenement

class EvenementForm(forms.ModelForm):
     class Meta:
        model = Evenement
        fields = ['title', 'description', 'image', 'slug']


class BlogCorporateForm(forms.ModelForm):
    class Meta:
        model = BlogCorporate
        fields = ['title', 'description', 'image', 'slug']

from .models import BlogConference

class BlogConferenceForm(forms.ModelForm):
    class Meta:
        model = BlogConference
        fields = ['title', 'description', 'image', 'slug']
    
   
    
      

        
        