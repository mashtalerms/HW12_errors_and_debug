from flask import Blueprint, render_template, request
from functions import load_posts_from_json, upload_posts
import logging

logging.basicConfig(encoding='utf-8', level=logging.INFO)

loader_blueprint = Blueprint('loader', __name__, url_prefix='/post', static_folder='static', template_folder='templates')
UPLOAD_FOLDER = "uploads/images"


@loader_blueprint.route('/form/')
def load_photo():
    return render_template('post_form.html')


@loader_blueprint.route('/upload/', methods=['POST'])
def upload():
    try:
        file = request.files['picture']
        filename = file.filename
        content = request.values['content']
        posts = load_posts_from_json()
        posts.append({
            'pic': f'uploads/images/{filename}',
            'content': content
        })
        upload_posts(posts)
        file.save(f'uploads/images/{filename}')
        if filename.split('.')[-1] not in ['png', 'jpeg', 'jpg']:
            logging.info('Файл не изображение')
    except FileNotFoundError:
        logging.error('Ошибка при загрузке файла')
        return '<h1>Файл не найден</h1><br><a href="/" class="link">Назад</a>'
    else:
        return render_template('post_uploaded.html', pic=f'/uploads/images/{filename}', content=content)

