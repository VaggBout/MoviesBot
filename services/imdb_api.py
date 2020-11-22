import requests
import json
import imdb
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
        if movie_details.get('plot'):
            plot = str(movie_details.get('plot'))
            index = plot.find('.')
            plot = plot[1:(index+1)]
        else:
            plot = 'Sorry, I could\'nt find the plot'
        
        rating = movie_details.get('rating') if movie_details.get('rating') else 'Sorry, I could\'nt find the rating'
        votes = movie_details.get('votes') if movie_details.get('votes') else 'Sorry, I could\'nt find the votes'

        info = {
            'title': movie.get('title'),
            'plot': plot,
            'rating': rating,
            'total_votes': votes
        }
        return info
    else:
        return None
        