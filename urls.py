from django.conf.urls import *
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^cluster/', include('zkadmin.urls')),
    url(r'^tree/', include('zktree.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),

    url(r'^', include('zkadmin.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
