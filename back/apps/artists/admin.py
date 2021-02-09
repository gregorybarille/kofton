from django.contrib import admin

# Register your models here.
from apps.artists.models import Artist
from apps.artists.models import Biography
from apps.artists.models import ArtistSocial
from apps.artists.models import Social
from apps.artists.models import Song
from apps.artists.models import SongSocial


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'visible']
    list_filter = ['visible']
    ordering = ['name']


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'artist', 'featured_name']
    list_filter = ['artist']
    ordering = ['artist', 'name']


@admin.register(Biography)
class BiographyAdmin(admin.ModelAdmin):
    list_display = ['artist', 'fr', 'en', 'de', 'es']
    ordering = ['artist']

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']


@admin.register(ArtistSocial)
class ArtistSocialAdmin(admin.ModelAdmin):
    list_display = ['social_network', 'link', 'artist']
    list_filter = ['artist']
    ordering = ['artist', 'social_network']


@admin.register(SongSocial)
class SongSocialAdmin(admin.ModelAdmin):
    list_display = ['social_network', 'link', 'song']
    list_filter = ['song']
    ordering = ['song', 'social_network']
