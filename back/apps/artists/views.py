import html
from django.http import JsonResponse
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from apps.artists.models import Artist, Song
from django.forms.models import model_to_dict


# Home
def index(request: HttpRequest) -> HttpResponse:
    # For Carousel > edit to do the last ones
    return render(request, "index.html")


def get_latest_songs(request: HttpRequest) -> HttpResponse:
    # For Carousel > edit to do the last ones
    latest_songs = Song.objects.all()
    return render(request, "base.html", {"songs": latest_songs})


# Used for Artists view
def fetch_artists(request: HttpRequest) -> HttpResponse:
    queryset = Artist.objects.all()
    artists = {artist for artist in queryset}
    return render(request, "artists.html", {"artists": artists})


# Used for artist specific page
def fetch_artist_details(request: HttpRequest, pk) -> HttpResponse:
    artist = get_object_or_404(Artist, pk=pk)
    language = request.LANGUAGE_CODE
    biographies = model_to_dict(artist.biography)
    artist_bio = biographies[language]
    artist_bio = html.unescape(artist_bio)
    artist_song = Song.objects.filter(artist=artist)
    return render(request, "artistdetail.html", {"artist": artist, "bio": artist_bio, "songs": artist_song})


# Contact form
def contact_form(request: HttpRequest) -> HttpResponse:
    return render(request, "contact.html")


def fetch_song(request: HttpRequest, pk) -> JsonResponse:
    if pk:
        queryset = Song.objects.get(id=pk)
    else:
        queryset = Song.objects.all().order_by("-release_date")
    response = {"song": [song.release_date for song in queryset]}
    return JsonResponse(response)
