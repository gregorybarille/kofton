import html
import json
from pathlib import Path
from django.core.management.base import BaseCommand
from django.core.files import File
from apps.artists.models import Artist, Biography, Song, ArtistSocial, Social, SongSocial


class Command(BaseCommand):
    def read_artistes_directory(self, artistes_informations):
        directory_list = Path('apps/artists/assets/Artistes').iterdir()
        for directory in directory_list:
            if directory.name != '.DS_Store':
                artiste_name = directory.name
                if Path(f'{directory}/bio.json').is_file:
                    with open(Path(f'{directory}/bio.json'), 'r') as json_file:
                        json_data = json.load(json_file)
                    artistes_informations["artistes"][artiste_name] = json_data
                    artistes_informations["sorties"].append({"artiste": artiste_name, "date": json_data["sortie"]["date_to_sort"]})

                else:
                    print(f'The bio.json file is missing for {artiste_name}')
                if Path(f'{directory}/bio.html').is_file:
                    with open(Path(f'{directory}/bio.html')) as html_file:
                        bio_content = html.escape(html_file.read())
                        artistes_informations["artistes"][artiste_name]['bio'] = bio_content
                else:
                    print(f'The bio.html file is missing for {artiste_name}')
                if Path(f'{directory}/images').is_dir():
                    for file_name in Path(f'{directory}/images').iterdir():
                        if "_artiste." in file_name.name:
                            artiste_image = file_name
                            artistes_informations["artistes"][artiste_name]['images'][
                                'artiste'] = artiste_image
                        elif "_bio." in file_name.name:
                            bio_image = file_name
                            artistes_informations["artistes"][artiste_name]['images'][
                                'bio'] = bio_image
                        elif "titre_" in file_name.name:
                            if "500" not in file_name.name:
                                if "1500" not in file_name.name:
                                    titre_image = file_name
                                    artistes_informations["artistes"][artiste_name]['images'][
                                        'titre'] = titre_image
                else:
                    print(f'The images folder is missing for {artiste_name}')
                new_artist = Artist.objects.update_or_create(name=artiste_name, image=File(open(artiste_image, 'rb')))
                new_artist_object = Artist.objects.get(name=artiste_name)
                new_bio = Biography.objects.update_or_create(artist=new_artist_object, fr=bio_content)
                if artistes_informations["artistes"][artiste_name]["social"]:
                    for social_network in artistes_informations["artistes"][artiste_name]["social"].keys():
                        artist_social_link = artistes_informations["artistes"][artiste_name]["social"][social_network]
                        social_object = Social.objects.get(name=social_network.capitalize())
                        artist_social = ArtistSocial.objects.update_or_create(artist=new_artist_object, social_network=social_object, link=artist_social_link)
                song_name = artistes_informations["artistes"][artiste_name]["sortie"]["titre"]
                song_featured = artistes_informations["artistes"][artiste_name]["sortie"]["artiste"]
                song_release_date = artistes_informations["artistes"][artiste_name]["sortie"]["date_to_sort"]
                if song_release_date:
                    song_day = song_release_date.partition('/')[0]
                    song_month = song_release_date.partition('/')[2].partition('/')[0]
                    song_year = song_release_date.partition('/')[2].partition('/')[2]
                    song_release_date = f'{song_year}-{song_month}-{song_day}'
                new_song = Song.objects.update_or_create(name=song_name, image=File(open(titre_image, 'rb')), artist=new_artist_object, featured_name=song_featured, release_date=song_release_date)
                new_song_object = Song.objects.get(name=song_name)
                if artistes_informations["artistes"][artiste_name]["sortie"]["platform"]:
                    for social_network in artistes_informations["artistes"][artiste_name]["sortie"]["platform"].keys():
                        social_link = artistes_informations["artistes"][artiste_name]["sortie"]["platform"][social_network]
                        print(social_network.title())
                        social_object = Social.objects.get(name=social_network.title())
                        SongSocial.objects.update_or_create(song=new_song_object, social_network=social_object, link=social_link)
        return artistes_informations
            

    def handle(self, *args, **kwargs):
        artistes_informations = {"artistes": {}, "sorties": []}
        artistes_informations = self.read_artistes_directory(artistes_informations)