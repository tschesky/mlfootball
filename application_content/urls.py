from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^settings$', views.settings, name='index'),
    url(r'^settings/password/$', views.password, name='index'),
    url(r'^register/$', views.register_page, name='register_page'),
]
