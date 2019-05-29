import html
import json
import os
from pathlib import Path
from datetime import datetime


def read_artistes_directory(artistes_informations):
    artistes_informations["sortie"] = []
    artiste_directory = './public/assets/Artistes'
    directory_list = Path('./public/assets/Artistes').iterdir()
    for directory in directory_list:
        if directory.name != '.DS_Store':
            artiste_name = directory.name
            print(artiste_name)
            if Path(f'{directory}/bio.json').is_file:
                with open(Path(f'{directory}/bio.json'), 'r') as json_file:
                    json_data = json.load(json_file)
                artistes_informations[artiste_name] = json_data
                artistes_informations["sortie"].append({"artiste": artiste_name, "date": json_data["sortie"]["date_to_sort"]})
            else:
                print(f'The bio.json file is missing for {artiste_name}')
            if Path(f'{directory}/bio.html').is_file:
                with open(Path(f'{directory}/bio.html')) as html_file:
                    bio_content = html.escape(html_file.read())
                    artistes_informations[artiste_name]['bio'] = bio_content
            else:
                print(f'The bio.html file is missing for {artiste_name}')
            if Path(f'{directory}/images').is_dir():
                if Path(f'{directory}/images/artiste.png').is_file():
                    artistes_informations[artiste_name]['images']['artiste'] = f'assets/Artistes/{artiste_name}/images/artiste.png'
                else:
                    print(f'The artiste.png file is missing for {artiste_name}')
                    artistes_informations[artiste_name]['images']['artiste'] = f'assets/Artistes/{artiste_name}/images/bio.png'
                if Path(f'{directory}/images/bio.png').is_file():
                    artistes_informations[artiste_name]['images']['bio'] = f'assets/Artistes/{artiste_name}/images/bio.png'
                else:
                    print(f'The bio.png file is missing for {artiste_name}')
                    artistes_informations[artiste_name]['images']['bio'] = f'assets/Artistes/{artiste_name}/images/artiste.png'
                if Path(f'{directory}/images/name.png').is_file():
                    artistes_informations[artiste_name]['images']['name'] = f'assets/Artistes/{artiste_name}/images/name.png'
                else:
                    print(f'The artiste.png file is missing for {artiste_name}')
                if Path(f'{directory}/images/titre.png').is_file():
                    artistes_informations[artiste_name]['images']['titre'] = f'assets/Artistes/{artiste_name}/images/titre.png'
                else:
                    print(f'The titre.png file is missing for {artiste_name}')
            else:
                print(f'The images folder is missing for {artiste_name}')


def sort_releases_by_dates(artistes_informations):
    print(artistes_informations["sortie"])
    artistes_informations["sortie"].sort(key=lambda x: datetime.strptime(x['date'], '%d/%m/%Y'), reverse=True)
    print(artistes_informations["sortie"])


def write_json(artistes_informations):
    with open('./public/data.json', 'w+') as file_json:
        json.dump(artistes_informations, file_json, sort_keys=True)


def main():
    artistes_informations = {}
    read_artistes_directory(artistes_informations)
    sort_releases_by_dates(artistes_informations)
    write_json(artistes_informations)


if __name__ == "__main__":
    main()
