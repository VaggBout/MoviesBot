from services import utils
from services import imdb_api
from services import data

async def event_search_movie(message):
    # TODO: Check if message is PM or from channel somehow
    await message.channel.send(data.resposnes.get('standby'))
    search_result = imdb_api.search_movie(utils.remove_prefix(message.content, '!search_movie'))
    
    if len(search_result) > 0:
        movie_info = imdb_api.get_movie_info(search_result[0])
        message_response = utils.movie_text_template(movie_info) 
        await message.channel.send(data.resposnes.get('found'))
        await message.channel.send(message_response)
    else:
        await message.channel.send(data.resposnes.get('not_found'))
