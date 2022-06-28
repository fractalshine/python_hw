# loader/views.py

# Добавим импорт шаблонизатора
from flask import render_template, Blueprint, request, send_from_directory
import time
from utils import write_json, create_post
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS

# Добавим настройку папки с шаблонами
loader_blueprint = Blueprint(
    'loader_blueprint',
    __name__,
    template_folder='templates',
)


@loader_blueprint.route("/post", methods=["GET", "POST"])
def page_post_form():
    return render_template("post_form.html")


@loader_blueprint.route("/post_uploaded", methods=["POST"])
def page_post_upload():
    # # Получаем объект картинки из формы
    # picture = request.files.get("picture")
    #
    # # Получаем текст из формы
    # text = request.form["content"]
    #
    # # Получаем имя файла у загруженного файла
    # filename = picture.filename
    # extension = filename.split(".")[-1]
    # time_str = time.strftime("%Y%m%d-%H%M%S")
    # time_filename = f"{time_str}.{extension}"
    # full_filename = f"{UPLOAD_FOLDER}/{time_filename}"
    #
    # # Собираем словарь
    # post_dict = {"uniq_img": f"{full_filename}",
    #              "content": text
    #              }
    # # Сохраняем картинку под уникальным именем в папку uploads
    # if is_filename_allowed(filename):
    #     picture.save(f"{full_filename }")
    #     pic = f"{full_filename}"
    #     write_json(post_dict)
    #
    #     return render_template("post_uploaded.html", pic=pic, cat_name=time_filename,
    #                            text=text)
    # else:
    #     extension = filename.split(".")[-1]
    #     return render_template("post_form_wrong_ext.html", ext=extension)
    pic, text, cat_name, template = create_post()
    return render_template(template, pic=pic, cat_name=cat_name,
                           text=text)


@loader_blueprint.route("/uploads/<path:path>")
def upload_dir(path):
    return send_from_directory("uploads", path)
