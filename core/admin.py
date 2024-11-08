from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.
from .models import Album, Photo,LivraisonPhoto,LivraisonAlbum

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'profile_pic', 'is_active',
                    'is_staff', 'is_superuser', 'last_login',)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2", "profile_pic"),
            },
        ),
    )
    
admin.site.register(CustomUser, CustomUserAdmin)



class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1  # Nombre de formulaires vides à afficher

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    inlines = [PhotoInline]

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo)

from .models import ServiceOrder

class ServiceOrderAdmin(admin.ModelAdmin):
    list_display = ('nom', 'postnom', 'email', 'service', 'date_commande', 'created_at')
    list_filter = ('service', 'date_commande')
    search_fields = ('nom', 'postnom', 'email')

admin.site.register(ServiceOrder, ServiceOrderAdmin)

class LivraisonPhotoInline(admin.TabularInline):
    model = LivraisonPhoto
    extra = 1  # Nombre de formulaires vides à afficher

class LivraisonAlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    inlines = [LivraisonPhotoInline]

admin.site.register(LivraisonAlbum, LivraisonAlbumAdmin)
admin.site.register(LivraisonPhoto)
