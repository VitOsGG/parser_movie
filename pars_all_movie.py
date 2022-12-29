import requests
from bs4 import BeautifulSoup
from time import sleep
import unicodedata
from pars_movie_id import movie_links_id


def all_movie():
    all_movie_data = []
    afisha_number = 1
    for m in movie_links_id:

        url_3 = f"https://ge.kinoafisha.info/movies/{m}/"
        sleep(2)
        r_3 = requests.get(url_3)
        soup_3 = BeautifulSoup(r_3.text, 'lxml')

        pict = soup_3.find('a', class_='filmInfo_posterLink').get('href')
        img_data = requests.get(pict, verify=False).content
        with open(f'afisha_movie/{afisha_number}.jpg', 'wb') as handler:
            handler.write(img_data)
        sleep(3)
        afisha_number += 1

        name = soup_3.find('h1', class_='trailer_title').text

        try:
            rating = soup_3.find('span', class_='rating_num').text
        except:
            rating = '-'

        coun = soup_3.find('span', class_='trailer_year').text[7:]
        ganre = soup_3.find('span', class_='filmInfo_genreItem button-main').text

        try:
            discr = unicodedata.normalize("NFKD", soup_3.find('div', class_='js-active').text).replace("\n",
                                                                                                       "").replace("\t",
                                                                                                                   "").replace(
                'Развернуть', '')
        except:
            discr = '-'

        all_movie_data.append([name, rating, coun, ganre, discr])

    return print(all_movie_data)


all_movie()
