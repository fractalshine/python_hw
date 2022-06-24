# loader/views.py

# Добавим импорт шаблонизатора
from flask import render_template, Blueprint, request, send_from_directory
import time
# Добавим настройку папки с шаблонами
loader_blueprint = Blueprint(
    'loader_blueprint',
    __name__,
    template_folder='../templates',
)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}


def is_filename_allowed(filename):
    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    return False


@loader_blueprint.route("/post", methods=["GET", "POST"])
def page_post_form():
    return render_template("post_form.html")


@loader_blueprint.route("/post_uploaded", methods=["POST"])
def page_post_upload():
    # Получаем объект картинки из формы
    picture = request.files.get("picture")

    # Получаем имя файла у загруженного файла
    filename = picture.filename
    extension = filename.split(".")[-1]
    timestr = time.strftime("%Y%m%d-%H%M%S")
    time_filename = f"{timestr}.{extension}"

    # Сохраняем картинку под родным именем в папку uploads
    if is_filename_allowed(filename):
        picture.save(f"./uploads/images/{time_filename}")
        pic = f"./uploads/images/{time_filename}"

        return render_template("post_uploaded.html", pic=pic, cat_name=time_filename)
    else:
        extension = filename.split(".")[-1]
        return render_template("post_form_wrong_ext.html", ext=extension)


@loader_blueprint.route("/uploads/<path:path>")
def upload_dir(path):
    return send_from_directory("uploads", path)
