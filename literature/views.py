from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from general.models import ArtWork, Comment
from literature.forms import WritingForm
from literature.models import Writing


def index(request):
    artworks = ArtWork.objects.all()
    pictures = []
    for artwork in artworks:
        if artwork.type == 'litra':
            comments = Comment.objects.filter(artwork=artwork)
            artwork.comments = comments
            pictures.append(artwork)
    return render(request, 'literature/index.html', {"artworks": pictures,})

def add_writing(request):
    if request.method == "GET":
        f = WritingForm()
        return render(request, 'literature/add.html', {"f": f, })
    elif request.method == "POST":
        f = WritingForm(request.POST)
        if f.is_valid():
            artwork = ArtWork()
            artwork.title = f.cleaned_data["title"]
            artwork.author = request.user.artuser
            artwork.pub_date = datetime.now()
            artwork.type = 'litra'
            artwork.save()
            writing = Writing()
            writing.artwork = artwork
            writing.content = f.cleaned_data["content"]
            writing.description = f.cleaned_data["description"]
            writing.save()
            return redirect(reverse('literature:index'))
    else:
        return HttpResponse("405")