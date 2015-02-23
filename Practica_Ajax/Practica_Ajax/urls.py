from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Practica_Ajax.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index$', 'misPruebas.views.index', name='index'),
    url(r'^ejemploajaxproceso$', 'misPruebas.views.ejemploajaxproceso', name='ejemploajaxproceso'),
    
)
