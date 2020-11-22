import requests
import json
import imdb
from services import utils
from imdb.Movie import Movie

imdb_data = imdb.IMDb()

def search_movie(keyword):
    if(keyword):
        return imdb_data.search_movie(keyword)
    else:
        return None
    

def get_movie_info(movie):
    if(movie):
        movie_details = imdb_data.get_movie(movie.movieID)
        summary = utils.generate_summary(movie_details.get('plot')) if  movie_details.get('plot') else 'Sorry, I could\'nt find the plot'
        rating = movie_details.get('rating') if movie_details.get('rating') else 'Sorry, I could\'nt find the rating'

        info = {
            'title': movie.get('title'),
            'plot': summary,
            'rating': rating
        }
        return info
    else:
        return None
        