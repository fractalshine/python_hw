from utils import get_dict_by_title, get_dict_by_year_range,\
    get_dict_by_auditory
from flask import Flask, jsonify
from errors_classes import ValueNotInAuditoryRange

app = Flask(__name__)


@app.route("/")
def main_page():
    return "начальная страница"


@app.route("/movie/by_tile/<title>")
def page_movies(title):
    return get_dict_by_title(title)


@app.route("/movie/by_years/<int:from_year>-<int:to_year>")
def page_years(from_year, to_year):
    result = get_dict_by_year_range(from_year, to_year)
    return jsonify(result)


@app.route("/movie/by_auditory/<auditory>")
def page_rating(auditory):
    result = get_dict_by_auditory(auditory)
    return jsonify(result)


@app.errorhandler(ValueNotInAuditoryRange)
def not_in_rating(e):
    return f'{e} '


if __name__ == '__main__':
    app.run(debug=True)
