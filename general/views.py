from datetime import datetime

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.shortcuts import render_to_response
from django.template.context_processors import csrf

from general.forms import ArtUserRegistrationForm
from general.models import ArtWork, Comment
from literature.forms import WritingForm, WritingUpdateForm
from music.forms import MTrackForm, MTrackUpdateForm
from pictures.forms import PictureForm, PictureUpdateForm


def index(request):
    artworks = ArtWork.objects.all().order_by("-pub_date")
    return render(request, 'general/index.html', {"artworks": artworks,})

def artwork_page(request, artwork_id):
    artwork = ArtWork.objects.get(id = artwork_id)
    if request.method == "GET":
        f = None
        if (artwork.type == "music"):
            f = MTrackUpdateForm()
        elif (artwork.type == "picture"):
            f = PictureUpdateForm()
        elif (artwork.type == "litra"):
            f = WritingUpdateForm()
        comments = Comment.objects.filter(art_work = artwork)
        return render(request, 'general/artwork_page.html', {'artwork': artwork, 'f': f, 'comments': comments})
    elif request.method == "POST":
        if request.user.is_authenticated():
            ctext = request.POST.get("text_comment")
            if len(ctext) == 0:
                return redirect(reverse('artwork', args=artwork_id))
            comment = Comment()
            comment.art_work = artwork
            comment.text = ctext
            comment.publisher = request.user.artuser
            comment.pub_date = datetime.now()
            comment.save()
            return redirect(reverse('artwork', args=(artwork_id,)))
        else:
            return redirect(reverse('artwork', args=artwork_id))

    else:
        return HttpResponse("405")

@login_required(login_url=reverse_lazy("login"))
def artwork_update(request, artwork_id):
    artwork = ArtWork.objects.get(id = artwork_id)
    if not request.user == artwork.author.user:
        return redirect(reverse('artwork', args=(artwork_id ,)))
    if request.method == "POST":
        f = None
        if (artwork.type == "music"):
            f = MTrackUpdateForm(request.POST, request.FILES)
            if f.is_valid():
                if len(f.cleaned_data["title"]) > 0:
                    artwork.title = f.cleaned_data["title"]
                artwork.save()
                mtrack = artwork.mtrack
                if not f.cleaned_data["image"] is None:
                    mtrack.image = f.cleaned_data["image"]
                if len(f.cleaned_data["description"]) > 0:
                    mtrack.description = f.cleaned_data["description"]
                mtrack.save()
        elif (artwork.type == "picture"):
            f = PictureUpdateForm(request.POST, request.FILES)
            if f.is_valid():
                if len(f.cleaned_data["title"]) > 0:
                    artwork.title = f.cleaned_data["title"]
                artwork.save()
                picture = artwork.picture
                if len(f.cleaned_data["description"]) > 0:
                    picture.description = f.cleaned_data["description"]
                picture.save()
        elif (artwork.type == "litra"):
            f = WritingUpdateForm(request.POST)
            if f.is_valid():
                if len(f.cleaned_data["title"]) > 0:
                    artwork.title = f.cleaned_data["title"]
                artwork.save()
                litra = artwork.literature
                if len(f.cleaned_data["description"]) > 0:
                    litra.description = f.cleaned_data["description"]
                litra.save()
        return redirect(reverse("artwork", args=(artwork_id,)))
    else:
        return HttpResponse("405")

def login(request):
    if request.user.is_authenticated():
        return redirect(reverse("pictures:index"))
    if request.method == "GET":
        context = {}
        if "next" in request.GET:
            context["next"] = "?next=" + request.GET["next"]
        return render(request, "general/login.html", context)
    elif request.method == "POST":
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        re = request.POST.get('remember_me')
        if user is not None:
            auth_login(request, user)
            if "next" in request.GET:
                h = redirect(request.GET["next"])
                if re != None:
                    h.set_cookie(key="remember", value=user.username, max_age=24*60*60)
                return h
            else:
                h = redirect(reverse("pictures:index"))
                if re != None:
                    h.set_cookie(key="remember", value=user.username, max_age=24*60*60)
                return h
        else:
            return redirect(reverse("index"))
    else:
        return HttpResponse("405")

@login_required()
def logout(request):
    auth_logout(request)
    return redirect(reverse("login"))


def register(request):
    if request.user.is_authenticated():
        return redirect(reverse("pictures:index"))
    if request.method == "GET":
        f = ArtUserRegistrationForm()
        return render(request, "general/register.html", {"f": f, })
    elif request.method == "POST":
        f = ArtUserRegistrationForm(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            return redirect('login')
        else:
            return render(request, 'general/register.html', {"f": f})
    else:
        return HttpResponse("405")