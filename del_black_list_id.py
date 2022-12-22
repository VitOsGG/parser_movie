from pars_movie_id import movie_links_id

black_list_id = ['8367938', '8367714', '7795867', '8364944', '8367552', '1623823']

for i in movie_links_id:
    if i in black_list_id:
        movie_links_id.remove(i)
print(len(movie_links_id))