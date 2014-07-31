from django.conf.urls import patterns, include, url
#from albums.views import AboutView, ArtistCreate

from albums.views import ArtistCreateView, ArtistUpdateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'musiclibrary.views.home', name='home'),
    # url(r'^musiclibrary/', include('musiclibrary.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url('^about/', AboutView.as_view()),
    url('^add/', ArtistCreateView.as_view(template_name='base.html')),
    url('^edit/', ArtistUpdateView.as_view(template_name='base.html')),
    )

