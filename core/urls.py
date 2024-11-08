from django.urls import path
from . import views 

urlpatterns = [
path('signup',views.signup, name='signup'),
path('signin',views.signin, name='signin'),
path('signout',views.signout, name='signout'),
path('profile',views.profile, name='profile'),
path('update_profile',views.update_profile, name='update_profile'),
path('album_list', views.album_list, name='album_list'),
path('album/<int:album_id>/', views.album_detail, name='album_detail'),
path('create/', views.create_album, name='create_album'),
path('album/<int:album_id>/upload/', views.upload_photo, name='upload_photo'),
path('photo/<int:photo_id>/download/', views.download_photo, name='download_photo'),
path('album/<int:album_id>/download/', views.download_album, name='download_album'),
path('album/<int:album_id>/delete/', views.delete_album, name='delete_album'),
path('photo/<int:photo_id>/delete/', views.delete_photo, name='delete_photo'),
path('service-order/', views.service_order, name='service_order'),
path('create-album/', views.create_livraison_album, name='create_livraison_album'),
path('add-photos/<int:album_id>/', views.add_photos, name='add_photos'),
path('album-detail/<int:album_id>/', views.livraison_album_detail, name='livraison_album_detail'),
]
