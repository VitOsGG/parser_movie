# parser_movie

![Python](https://img.shields.io/badge/Python-3.11.0-yellow) ![aiogram](https://img.shields.io/badge/BeautifulSoup-blue) ![aiogram](https://img.shields.io/badge/requests-blue) ![aiogram](https://img.shields.io/badge/unicodedata-blue) ![aiogram](https://img.shields.io/badge/sleep-blue) ![aiogram](https://img.shields.io/badge/lxml-blue)

___

Проект создан для парсинка сайта с фильмами. В дальнейшем информация о фильмах используется для создания базы данных фильмов, которая в свою очередь используется в проекте telegram-бота. 

Ссылка на проект telegram-боте и проект создания БД:
* [Проект telegram-бота по подбору фильмов](https://github.com/VitOsGG/search_movie_telegram_bot)
* [Проект создания БД](https://github.com/VitOsGG/create_db_movie)

___
**Структура проекта:**

* Папка venv

Стандартная папка с виртуальный окружением для установки необходимых библиотек (список всех библиотек хранится в документе requirements.txt)

* Папка afisha_movie

Папка в которую загружаются афиши фильмов при парсинге

* Файлы в корневой папке:

  * pars_one_movie.py - файл парсинга определенной информации с страницы одного фильма 
  
  * pars_movie_id.py - файл парсинга id фильмов из URL каждого фильма
    
  * del_black_list_id.py - файл в котором выполняется удаление id нежелательных фильмов
  
  * pars_all_movie.py - файл парсинга информации фильмов по их id
   
  * all_movie.py - файл с списком фильмов и информации о каждом фильме
  
* Реализация 
  
  -Файл pars_one_movie.py. Парсинг информации одного фильма:
  
  Считываем страницу
  
  ```python
  url_2 = "https://www.kinoafisha.info/movies/5227/"
    r_2 = requests.get(url_2, timeout=5)

    soup_2 = BeautifulSoup(r_2.text, 'lxml')
  ```
  
  Скачиваем афишу
  
  ```python
  pict = soup_2.find('a', class_='filmInfo_posterLink').get('href')
    afisha_number = 1
    img_data = requests.get(pict, verify=False).content
    with open(f'{afisha_number}.jpg', 'wb') as handler:
        handler.write(img_data)
  ```
  
  Считываем остальную информацию (название, рейтинг, страну, жанр, описание):
  
  ```python
  name = soup_2.find('h1', class_='trailer_title').text

    try:
        rating = soup_2.find('span', class_='rating_num').text
    except:
        rating = '-'

    coun = soup_2.find('span', class_='trailer_year').text[7:]
    ganre = soup_2.find('span', class_='filmInfo_genreItem button-main').text
    discr = unicodedata.normalize("NFKD", soup_2.find('div', class_='js-active').text).replace("\n", "").\
        replace("\t", "").replace('Развернуть', '')
  ```
  
  -Файл pars_movie_id.py. Получаем id необходимых фильмов:
  ```python
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
  ```
  
  -Файл del_black_list_id.py. Удаляем id нежелательных фильмов:
  ```python
  black_list_id = ['8367938', '8367714', '7795867', '8364944', '8367552', '1623823']

  for i in movie_links_id:
    if i in black_list_id:
        movie_links_id.remove(i)
  print(len(movie_links_id))
  ```
  
  -Файл pars_all_movie.py. Производим парсинг фмльмов по id:
  ```python
  all_movie_data = []
  afisha_number = 1
  for m in movie_links_id:

      url_3 = f"https://ge.kinoafisha.info/movies/{m}/"
      sleep(2)
      r_3 = requests.get(url_3)
      soup_3 = BeautifulSoup(r_3.text, 'lxml')
      /
      /
      /
   ```
   Код отображен не полность. Код такой как в файле pars_one_movie.py, только с помощью цикла подставляем в URL необходимый id фильма из списка.
  
  
  
  
  
  
  
