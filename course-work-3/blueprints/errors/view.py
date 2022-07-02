from flask import render_template, Blueprint

# Добавим настройку директории с шаблонами
error_blueprint = Blueprint(
    'error_blueprint',
    __name__,
)


@error_blueprint.app_errorhandler(413)
def page_not_found(e):
    return f'File to big: {e}'


@error_blueprint.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
