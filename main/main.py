from flask import Blueprint, request, render_template
from functions import load_posts_from_json
import logging

logging.basicConfig(encoding='utf-8', level=logging.INFO)

main_blueprint = Blueprint('main', __name__, url_prefix='/', template_folder='templates')


@main_blueprint.route('/')
def show_photo():
    return render_template("index.html")


@main_blueprint.route('/search/')
def search_post():
    search_by = request.args['s']
    logging.info(f'Слово для поиска: {search_by}')
    posts = [x for x in load_posts_from_json() if search_by.lower() in x['content'].lower()]
    return render_template('post_list.html', search_by=search_by, posts=posts)
