import requests
from bs4 import BeautifulSoup
from time import sleep

movie_links_id = []

for z in range(10):
    print(z)

    url_1 = f"https://www.kinoafisha.info/rating/movies/?page={z}"
    sleep(5)
    r_1 = requests.get(url_1, timeout=5)
    soup_1 = BeautifulSoup(r_1.text, 'lxml')

    films = soup_1.find_all('div', class_='movieItem')
    for film in films:
        link = film.find('a', 'movieItem_title').get('href')
        link = ''.join([i for i in link if i.isdigit()])
        movie_links_id.append(link)

