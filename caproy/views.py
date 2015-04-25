from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth


def index(request):
    return render(request, "caproy/index.html", {'signed_in': request.user.is_authenticated()})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "caproy/register.html", {
        'form': form,
    })

def sign_in(request):
    sign_in_failed = False
    if request.method == 'POST':
        # see http://www.djangobook.com/en/2.0/chapter14.html
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect("/")
        else:
            sign_in_failed = True
    # Sign-in page
    return render(request, "caproy/sign-in.html", {"sign_in_failed": sign_in_failed})

def sign_out(request):
    auth.logout(request)
    return render(request, "caproy/sign-out.html")

def profile(request):
    return render(request, "caproy/profile.html")

def game(request):
    return render(request, "caproy/game.html")

#API:
#def castle(request, user):
#    #Handle post if user is current logged in user, or get for any logged in users
#    pass
