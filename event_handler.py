from services import utils
from services import imdb_api
from services import data

async def event_search_movie(message):
    # TODO: Check if message is PM or from channel somehow
    search_terms = utils.remove_prefix(message.content, data.commands.get('movie_search'))
    if search_terms.isspace() or not search_terms:
        await message.channel.send(data.resposnes.get('no_args_movie'))
        return
        
    await message.channel.send(data.resposnes.get('standby'))
    search_result = imdb_api.search_movie(search_terms)
    
    if search_result:
        movie_info = imdb_api.get_movie_info(search_result[0])
        if movie_info:
            await message.channel.send(data.resposnes.get('found'))
            message_response = utils.movie_text_template(movie_info) 
            await message.channel.send(message_response)
        else:
            await message.channel.send(data.resposnes.get('not_found'))
    else:
        await message.channel.send(data.resposnes.get('not_found'))
