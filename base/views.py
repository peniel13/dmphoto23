from django.shortcuts import render,redirect, get_object_or_404
from .forms import ContactForm,TestimonialForm,CommentForm,BlogVideoForm, BlogMariageForm
from django.contrib import messages
from .models import Testimonial,Blog, Comment,Contact1,BlogVideo,BlogCulinaire,Evenement,BlogMariage,BlogFamille
from django.views.generic import ListView, DetailView
from django.views import View
import string 
 

class BlogListView(ListView):
    model = Blog
    template_name = 'base/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 6 
    def get_queryset(self):
        return Blog.objects.all().order_by('-created')
    
class BlogDetailView(DetailView):
    model = Blog
    template_name = 'base/blog_detail.html'
    context_object_name = 'blog'

class AddCommentView(View):
    def post(self, request, slug):
        blog = get_object_or_404(Blog, slug=slug)
        comment = Comment(
            body=request.POST['body'],
            blog=blog,
            user=request.user
        )
        comment.save()
        return redirect('blog_detail', slug=slug)



def index(request):
    testimonials = Testimonial.objects.all().order_by('-created_at')
    blogs = Blog.objects.all().order_by('-created')[:3]  # Récupération des trois derniers blogs

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        content = request.POST.get('content')

        # Validation logic
        if len(name) < 2 or len(name) > 30:
            messages.error(request, 'Length of Name should be greater than 2 and less than 30')
        elif len(email) < 5 or len(email) > 30:
            messages.error(request, 'Email is not correct, try again!')
        elif len(number) < 10 or len(number) > 12:
            messages.error(request, 'Number not correct, try again!')
        else:
            ins = Contact1(name=name, email=email, content=content, number=number)
            ins.save()
            messages.success(request, 'Thank You for contacting us! Your message has been saved.')

    return render(request, 'base/index.html', {'testimonials': testimonials, 'blogs': blogs})



# views.py



from django.contrib import messages

def submit_testimonial(request):
    user = request.user  # Récupération de l'utilisateur connecté
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = user  # Associer le témoignage à l'utilisateur
            testimonial.save()
            messages.success(request, "Témoignage soumis avec succès !")  # Message de succès
            return redirect('profile')  # Redirige vers la page de profil ou la page souhaitée
    else:
        form = TestimonialForm()
    
    testimonials = Testimonial.objects.all().order_by('-created_at')  # Récupération des témoignages
    return render(request, 'base/submit_testimonials.html', {'form': form, 'testimonials': testimonials})

punc = string.punctuation  
def contact1(request):
    # return HttpResponse('contact')
    if request.method=="POST":
        print('post')
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        content = request.POST['content']
        print(name,email,content,number)
        if len(name) >1 and len(name) < 30:
            pass
        else:
            messages.error(request,'length of Name should be greater than 2 and less than 30')
            return render(request,'base/contact.html')

        if len(email) >1 and len(email) < 30:
            pass
        else:
            messages.error(request,'email is not correct try again!!')
            return render(request,'base/contact.html')
        print(len(number))
        if len(number) > 9 and len(number) < 13:
            pass
        else:
            messages.error(request,'number not correct try again!!')
            return render(request,'base/contact.html')
        ins = Contact1(name=name,email=email,content=content,number=number)
        ins.save()
        messages.success(request,'Thank You for contacting me!! Your message has been saved ')
        print('data has been saved to database')
    else:
        print('not post')
    return render(request,'base/contact.html')


def photocop(request):
    # Récupérer tous les blogs de photographie immobilière
    blogs = BlogPhoto.objects.all()
    return render(request, 'base/photo.html', {'blogs': blogs})

from .models import BlogPhoto


def video(request):
    # Récupérer la vidéo "featured" (en vedette)
    featured_video = BlogVideo.objects.filter(featured=True).first()

    # Récupérer toutes les vidéos pour la galerie
    videos = BlogVideo.objects.all()

    # Passer la vidéo "featured" et la liste des vidéos au template
    return render(request, 'base/video.html', {
        'featured_video': featured_video,
        'videos': videos
    })



def mariage(request):
    if request.method == 'POST':
        form = BlogMariageForm(request.POST, request.FILES)  # Inclure request.FILES pour traiter l'image
        if form.is_valid():
            form.save()  # Sauvegarder le blog de mariage
            return redirect('mariage')  # Redirige après la soumission
    else:
        form = BlogMariageForm()

    blogs = BlogMariage.objects.all()  # Récupérer les blogs de mariage existants
    return render(request, 'base/mariage.html', {'form': form, 'blogs': blogs})


from .models import BlogCorporate

def corporate(request):
    # Récupérer tous les blogs corporate depuis la base de données
    blogs = BlogCorporate.objects.all()

    # Passer les blogs au template
    return render(request, 'base/corporate.html', {'blogs': blogs})


from .models import BlogConference  # Assure-toi que ce modèle existe

def conference(request):
    # Récupérer tous les blogs conférence depuis la base de données
    blogs = BlogConference.objects.all()

    # Passer les blogs au template
    return render(request, 'base/conference.html', {'blogs': blogs})


def famille(request):
    # Récupère toutes les photos de famille
    blogs = BlogFamille.objects.all()
    
    # Passe les objets Famille au template
    return render(request, 'base/famille.html', {'blogs': blogs})

def evenement(request):
    # Récupère tous les événements à venir (triés par date)
    blogs = Evenement.objects.all() # Filtre pour les événements à venir
    return render(request, 'base/evenement.html', {'blogs': blogs})

def culinaire(request):
    # Récupérer tous les blogs culinaires depuis la base de données
    blogs = BlogCulinaire.objects.all()

    # Passer les blogs au template
    return render(request, 'base/culinaire.html', {'blogs': blogs})


def apropos(request):
    return render(request,'base/apropos.html')

# def add_blog_video(request):
#     if request.method == 'POST':
#         form = BlogVideoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('blog_video_list')  # Redirige vers une liste de vidéos ou une autre vue après la soumission
#     else:
#         form = BlogVideoForm()
    
#     return render(request, 'add_video.html', {'form': form})

