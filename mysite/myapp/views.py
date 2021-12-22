from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.generic import CreateView
from .models import Song
from .forms import SongForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm




class SongCreate(CreateView):
    model = Song
    form_class = SongForm 
    extra_context = {'songs': Song.objects.all()}
    template_name = 'song_create.html'
    success_url = '/songs/'

def home_page(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['myfile1']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)
        return render(request, 'home_page.html', {
            'file_url': file_url
        })
    return render(request, 'home_page.html')

#def home_page(request):
    #data = Song.objects.all()
    #return render(request, 'home_page.html', {'data': data})

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


