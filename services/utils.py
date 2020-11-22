import os
import re
from typing import Text

def remove_prefix(str, prefix):
    return str.lstrip(prefix)

# Generates a summary of plot using OTS(Open-Text-Summarizer)
def generate_summary(sentences):
    # Clean text
    text = ''
    for sentence in sentences:
        sentence = re.sub('::.*', '', sentence)
        text += sentence

    f = open("plot.txt", "w+")
    f.write(text)
    f.close()

    summary_percentage = os.getenv('summary_percentage')
    stream = os.popen('ots --ratio '+summary_percentage+' plot.txt')
    summary = stream.read()
    summary = summary.replace('.', '. ')

    return summary

def movie_text_template(movie_info):
    response = (
                'Title: ' +str(movie_info.get('title'))
                +'\nScore: '+str(movie_info.get('rating'))
                +'\nSummary: '+str(movie_info.get('plot'))
                )
    return response