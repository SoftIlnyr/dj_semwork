from datetime import datetime
from time import timezone

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from general.models import ArtWork
from pictures.forms import PictureForm
from pictures.models import Picture


def index(request):
    artworks = ArtWork.objects.all()
    pictures = []
    for artwork in artworks:
        if artwork.type == 'picture':
            pictures.append(artwork)
    return render(request, 'pictures/index.html', {"artworks": pictures,})

def add_picture(request):
    if request.method == "GET":
        f = PictureForm()
        return render(request, 'pictures/add.html', {"f": f, })
    elif request.method == "POST":
        f = PictureForm(request.POST, request.FILES)
        if f.is_valid():
            artwork = ArtWork()
            artwork.title = f.cleaned_data["title"]
            artwork.author = request.user.artuser
            artwork.pub_date = datetime.now()
            artwork.type = 'picture'
            artwork.save()
            picture = Picture()
            picture.artwork = artwork
            picture.content = f.cleaned_data["content"]
            picture.description = f.cleaned_data["description"]
            picture.save()
            return redirect(reverse('pictures:index'))
    else:
        return HttpResponse("405")