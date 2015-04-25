from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register.html', views.register, name='register'),
    url(r'^profile.html', views.profile, name='profile'),
    url(r'^game.html', views.game, name='game'),
    url(r'^sign-in.html', views.sign_in, name='sign_in'),
    url(r'^sign-out.html', views.sign_out, name='sign_out'),
]
