from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('contact/', views.contact1, name='contact'),
    path('apropos/', views.apropos, name='apropos'),
    path('mariage/', views.mariage, name='mariage'),
    path('photo/', views.photocop, name='photo'),
    path('corporate/', views.corporate, name='corporate'),
    path('conference/', views.conference, name='conference'),
    path('famille/', views.famille, name='famille'),
    path('evenement/', views.evenement, name='evenement'),
    path('culinaire/', views.culinaire, name='culinaire'),
    path('videos/', views.video, name='video'),
    path('soumettre/', views.submit_testimonial, name='submit_testimonial'),
    path('blog/', views.BlogListView.as_view(), name='blog_list'),
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('blog/<slug:slug>/comment/', views.AddCommentView.as_view(), name='add_comment'),
    
]
