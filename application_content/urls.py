from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='index')),
    url(r'^index$', views.index, name='index'),
    url(r'^news$', views.news, name='news'),
    url(r'^news$', views.index, name='index'),
    url(r'^results$', views.results, name='results'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^settings/password$', views.password, name='password'),
    url(r'^register/$', views.register_page, name='register_page'),
]
