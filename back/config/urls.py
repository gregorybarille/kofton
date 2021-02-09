"""koftonmusic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls.i18n import i18n_patterns

from apps.artists.views import index
from apps.artists.views import fetch_artist_details
from apps.artists.views import fetch_artists
from apps.artists.views import get_latest_songs
from apps.artists.views import contact_form
from config import settings

urlpatterns = [path("admin/", admin.site.urls)]

urlpatterns  = [
    path("", index, name="index"),
    path("artists/", fetch_artists, name="fetch_artists"),
    path("artists/<int:pk>", fetch_artist_details, name="fetch_artists_details"),
    path("contact/", contact_form, name="contact_form"),
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
