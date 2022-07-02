# main/views.py

# Добавим импорт шаблонизатора
from flask import render_template, Blueprint, request
from utils import validate_json, get_posts_by_word

# Добавим настройку папки с шаблонами
main_blueprint = Blueprint(
    'main_blueprint',
    __name__,
    # template_folder='templates',
)


# Добавим render_template
@main_blueprint.route('/')
def main_page():
    template, text, posts = validate_json()
    return render_template(template, posts=posts, text=text)


# Добавим render_template
@main_blueprint.route('/search')
def search_page():
    s = request.args['s']
    posts = get_posts_by_word(s)

    return render_template("post_list.html", posts=posts, search=s)

