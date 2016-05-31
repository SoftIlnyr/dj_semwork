from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.shortcuts import render_to_response
from django.template.context_processors import csrf

from general.forms import ArtUserRegistrationForm


def login(request):
    if request.user.is_authenticated():
        return redirect(reverse("music:index"))
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
                h = redirect(reverse("music:index"))
                if re != None:
                    h.set_cookie(key="remember", value=user.username, max_age=24*60*60)
                return h
        else:
            return redirect(reverse("login"))
    else:
        return HttpResponse("405")

@login_required()
def logout(request):
    auth_logout(request)
    return redirect(reverse("login"))


def register(request):
    if request.user.is_authenticated():
        return redirect(reverse("music:index"))
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