import json
import time
from flask import request
from config import ALLOWED_EXTENSIONS, UPLOAD_FOLDER, \
    logger, POST_PATH


def load_json(filepath):
    """Выгружаем посты в список из файла"""

    with open(filepath, 'r', encoding='utf-8') as f:
        raw_json = f.read()

    post_list = json.loads(raw_json)

    return post_list


def load_posts() -> list:
    """Выгружаем посты в список из файла"""

    post_list = load_json(POST_PATH)

    return post_list


def validate_json() -> tuple:
    try:
        posts = reversed(load_posts())
        template = "index.html"
        return template, None, posts
    except FileNotFoundError as error:
        template = "index_errorpage.html"
        text = "Файл базы данных не найден"
        logger.error(f"{text}, original error - {error}")
        return template, text, None
    except json.JSONDecodeError as error:
        template = "index_errorpage.html"
        text = "Файл базы данных имеет неподходящий формат"
        logger.error(f"{text}, {error}")
        return template, text, None


def is_filename_allowed(filename) -> bool:
    """Проверка на расширение"""

    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    # return False


# function to add to JSON
def write_json(new_data, filename=POST_PATH):
    with open(filename, 'r+', encoding='utf-8') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, ensure_ascii=False,
                  indent=2)


def get_posts_by_word(user_input):
    """"Получаем список постов по слову из формы поиска"""

    dict_list = load_posts()
    user_input_lower = user_input.lower()
    search_list = []
    template = "posts_list.html"

    if user_input == "":
        message = "Вы ничего не ввели"
        template = "index.html"
        return message, template

    for dictionary in dict_list:
        post = dictionary['content'].lower()
        if user_input_lower in post:
            search_list.append(dictionary)
            continue
    return search_list, template


def get_post_by_uid(uid):
    dict_list = load_posts()

    for d in dict_list:
        if uid == d['pk']:
            return d

def create_post() -> tuple:
    picture = request.files.get("picture")
    text = request.form["content"]
    filename = picture.filename
    extension = filename.split(".")[-1]
    time_str = time.strftime("%Y%m%d-%H%M%S")
    time_filename = f"{time_str}.{extension}"
    full_filename = f"{UPLOAD_FOLDER}/{time_filename}"

    post_dict = {"uniq_img": f"{full_filename}",
                 "content": text
                 }
    template = "post_uploaded.html"

    if text == "":
        text = "Вы ничего не ввели"
        template = "post_form_wrong_ext.html"
        logger.info(f"{text}")
        return None, text, None, template

    if not picture:
        text = "Вы не выбрали картинку"
        template = "post_form_wrong_ext.html"
        logger.info(f"{text}")
        return None, text, None, template

    if not is_filename_allowed(filename):
        text = f"Расширение {extension} не поддерживается"
        template = "post_form_wrong_ext.html"
        logger.info(f"{text}")
        return None, text, None, template

    picture.save(f"{full_filename}")
    write_json(post_dict)

    return full_filename, text, time_filename, template
