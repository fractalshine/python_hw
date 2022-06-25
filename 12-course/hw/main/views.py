# main/views.py

# Добавим импорт шаблонизатора
from flask import render_template, Blueprint, request
from utils import load_json

# Добавим настройку папки с шаблонами
main_blueprint = Blueprint(
    'main_blueprint',
    __name__,
    # template_folder='templates',
)


# Добавим render_template
@main_blueprint.route('/')
def main_page():
    posts = reversed(load_json())
    return render_template("index.html", posts=posts)


# Добавим render_template
@main_blueprint.route('/search')
def search_page():
    s = request.args['s']
    return render_template("post_list.html")

