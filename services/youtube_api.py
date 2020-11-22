from youtube_api import YoutubeDataApi
from dotenv import load_dotenv
import os

load_dotenv()
yt_token = os.getenv('youtube_token')
yt_watch_base_url = 'https://www.youtube.com/watch?v='

yt = YoutubeDataApi(yt_token)

def get_trailer_url(movie_title):
    search_result = yt.search(q=movie_title+' trailer', max_results=1, search_type="video")
    if search_result and len(search_result) > 0:
        trailer_url = yt_watch_base_url + search_result[0]['video_id']
        return trailer_url
    else:
        return None