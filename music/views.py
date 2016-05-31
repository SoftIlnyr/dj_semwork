from datetime import datetime
from time import timezone

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from general.models import ArtWork
from music.forms import MTrackForm
from music.models import MTrack


def index(request):
    artworks = ArtWork.objects.all()
    mtracks = []
    for artwork in artworks:
        if artwork.type == 'music':
            mtracks.append(artwork)
    return render(request, 'music/index.html', {"artworks": mtracks,})

def add_mtrack(request):
    if request.method == "GET":
        f = MTrackForm()
        return render(request, 'music/add.html', {"f": f, })
    elif request.method == "POST":
        f = MTrackForm(request.POST, request.FILES)
        if f.is_valid():
            artwork = ArtWork()
            artwork.title = f.cleaned_data["title"]
            artwork.author = request.user.artuser
            artwork.pub_date = datetime.now()
            artwork.type = 'music'
            artwork.save()
            mtrack = MTrack()
            mtrack.artwork = artwork
            mtrack.content = f.cleaned_data["content"]
            mtrack.image = f.cleaned_data["image"]
            mtrack.description = f.cleaned_data["description"]
            mtrack.save()
            return redirect(reverse('music:index'))
    else:
        return HttpResponse("405")