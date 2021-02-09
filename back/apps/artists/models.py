from django.db import models
from ckeditor.fields import RichTextField


def define_bio_image(instance, filename: str) -> str:
    return f"{instance.name}/{instance.name}_bio.png"


def define_song_image(instance, filename: str) -> str:
    return f"{instance.artist.name}/{instance.name}_titre.png"


def define_social_image(instance, filename: str) -> str:
    return f"{instance.name}/{instance.name}_logo.png"


class Artist(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    image = models.ImageField(blank=False, upload_to=define_bio_image)
    visible = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Social(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    logo = models.ImageField(blank=False, upload_to=define_social_image)

    def __str__(self):
        return self.name


class Biography(models.Model):
    artist = models.OneToOneField(Artist, on_delete=models.CASCADE, related_name="biography")
    fr = RichTextField()
    en = RichTextField()
    de = RichTextField()
    es = RichTextField()

    def __str__(self):
        return f"Bio {self.artist}"


class ArtistSocial(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="socials")
    social_network = models.ForeignKey(Social, on_delete=models.CASCADE, related_name="artist_social_network")
    link = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"{self.artist.name}, {self.social_network.name}: {self.link}"


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="songs")
    name = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(blank=False, upload_to=define_song_image)
    featured_name = models.CharField(max_length=255, null=True, blank=True)
    release_date = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.name


class SongSocial(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="socials")
    social_network = models.ForeignKey(Social, on_delete=models.CASCADE, related_name="song_social_network")
    link = models.CharField(max_length=255, null=False, blank=False)
