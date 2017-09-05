import random

from marvelator.characters_resource import CharactersResource
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def get_random_comic_page():
    # attributionHTML
    attribution_html = None

    # get only the first 100 comics, as it can take a long time
    comics = CharactersResource(1009515).comics(100)

    # choose a random comic from the list
    random_comic = random.choice(comics)

    # get all the featured chars
    char_list = []
    characters_id_list = [char['resourceURI'][-7:] for char in random_comic['characters']['items']]

    for char_id in characters_id_list:
        char = CharactersResource(char_id).get()
        char_list.append({'name': char.name, 'thumbnail': char.thumbnail['path'] + '.' + char.thumbnail['extension']})

        if not attribution_html:
            attribution_html = char.attributionHTML

    return render_template('comic.html', context={'comic': random_comic,
                                                   'featured_chars': char_list,
                                                   'attributionHTML': attribution_html})

if __name__ == '__main__':
    app.run()