def remove_prefix(str, prefix):
    return str.lstrip(prefix)

def movie_text_template(movie_info):
    response = (
                'Title: ' +str(movie_info.get('title'))
                +'\nScore: '+str(movie_info.get('rating'))
                +'\nTotal Votes: '+str(movie_info.get('votes'))
                +'\nSummary: '+str(movie_info.get('plot'))
                )
    return response