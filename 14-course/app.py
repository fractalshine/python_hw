from utils import get_dict_by_title
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/movie/<title>")
def page_movies(title):
    return jsonify(get_dict_by_title(title))


app.run()
