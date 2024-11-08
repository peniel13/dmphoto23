# admin.py
from django.contrib import admin
from .models import Contact,Blog,Category,Comment,Contact1,CategoryVideo,BlogCorporate
from .forms import Contact1Form

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'message')

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Comment)

from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'content_preview', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'content')  # Assuming you want to search by username too
    ordering = ('-created_at',)

    def get_username(self, obj):
        return obj.user.username if obj.user else 'Anonyme'  # Safely handle None
    get_username.short_description = 'Utilisateur'  # Set a friendly name for the column

    def content_preview(self, obj):
        return obj.content[:50]  # Display the first 50 characters
    content_preview.short_description = 'Aperçu du contenu'

@admin.register(Contact1)
class Contact1Admin(admin.ModelAdmin):
    form = Contact1Form  # Utiliser le formulaire personnalisé
    list_display = ('name', 'email', 'number')  # Champs à afficher dans la liste
    search_fields = ('name', 'email')  # Champs de recherche
    ordering = ('name',)

from .models import BlogVideo, Category
from .forms import BlogVideoForm

# Pour afficher le modèle BlogVideo dans l'admin avec un formulaire personnalisé
class BlogVideoAdmin(admin.ModelAdmin):
    form = BlogVideoForm  # Utilise le formulaire personnalisé
    list_display = ('title', 'slug', 'categoryvideo', 'featured', 'created', 'updated')
    search_fields = ('title', 'category__title')
    list_filter = ('categoryvideo', 'featured')
    prepopulated_fields = {'slug': ('title',)}  # Pour générer automatiquement le slug
    ordering = ('-created',)  # Afficher les vidéos dans l'ordre décroissant de création
    readonly_fields = ('created', 'updated')  # Ne pas autoriser la modification des champs 'created' et 'updated'

admin.site.register(BlogVideo, BlogVideoAdmin)
admin.site.register(CategoryVideo)  # Si tu veux afficher Category dans l'admin également


from .models import BlogFamille


from .models import BlogMariage

class BlogMariageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'slug', 'image')  # Afficher l'image dans la liste
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')
    list_filter = ('created_at',)

admin.site.register(BlogMariage, BlogMariageAdmin)


from .models import BlogPhoto

class BlogPhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'slug', 'image')  # Inclure 'image' dans la liste
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')
    list_filter = ('created_at',)

admin.site.register(BlogPhoto, BlogPhotoAdmin)

from .models import BlogCulinaire

class BlogCulinaireAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'slug', 'image')  # Inclure 'image' dans la liste
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')
    list_filter = ('created_at',)
admin.site.register(BlogCulinaire, BlogCulinaireAdmin)

class BlogFamilleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'slug', 'image')  # Inclure 'image' dans la liste
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')
    list_filter = ('created_at',) # Ajouter un filtre basé sur la date de création

admin.site.register(BlogFamille, BlogFamilleAdmin)

from .models import Evenement

class EvenementAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'slug', 'image')  # Inclure 'image' dans la liste
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')
    list_filter = ('created_at',)
admin.site.register(Evenement, EvenementAdmin)


class BlogCorporateAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'slug', 'image')  # Inclure 'image' dans la liste
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')
    list_filter = ('created_at',)

admin.site.register(BlogCorporate, BlogCorporateAdmin)

from .models import BlogConference

class BlogConferenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'slug', 'image')  # Inclure 'image' dans la liste
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')
    list_filter = ('created_at',)

admin.site.register(BlogConference, BlogConferenceAdmin)
   


