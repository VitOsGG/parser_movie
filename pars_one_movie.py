import requests
from bs4 import BeautifulSoup
import unicodedata


def one_movie():
    url_2 = "https://www.kinoafisha.info/movies/5227/"
    r_2 = requests.get(url_2, timeout=5)

    soup_2 = BeautifulSoup(r_2.text, 'lxml')

    pict = soup_2.find('a', class_='filmInfo_posterLink').get('href')
    afisha_number = 1
    img_data = requests.get(pict, verify=False).content
    with open(f'{afisha_number}.jpg', 'wb') as handler:
        handler.write(img_data)

    name = soup_2.find('h1', class_='trailer_title').text

    try:
        rating = soup_2.find('span', class_='rating_num').text
    except:
        rating = '-'

    coun = soup_2.find('span', class_='trailer_year').text[7:]
    ganre = soup_2.find('span', class_='filmInfo_genreItem button-main').text
    discr = unicodedata.normalize("NFKD", soup_2.find('div', class_='js-active').text).replace("\n", "").\
        replace("\t", "").replace('Развернуть', '')

    return name, rating, coun, ganre, discr


one_movie()