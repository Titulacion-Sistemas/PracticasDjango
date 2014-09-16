from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.auth.views import login, logout
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from usuarios.views import multiply

dajaxice_autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'usuarios_logueados.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'usuarios.views.main', name='main'),
    url(r'^signup$', 'usuarios.views.signup', name='signup'),
    url(r'^login$', login, {'template_name': 'login.html', }, name="login"),
    url(r'^home$', 'usuarios.views.home', name='home'),
    url(r'^logout$', logout, {'template_name': 'main.html', }, name="logout"),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^multiply', multiply),
)
