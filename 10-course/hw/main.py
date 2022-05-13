from utils import load_candidates
from flask import Flask

app = Flask(__name__)


@app.route("/")
def page_index():
    candidates_list = load_candidates()
    string = ""
    for dictionary in candidates_list:
        string += "Имя кандидата - " + dictionary['name'] + "\n" + \
                  "Позиция кандидата - " + dictionary['position'] + "\n" + \
                  "Навыки через запятую: " + dictionary['skills'] + "\n" + \
                  "" + "\n"
    return f'{"<pre>" + string + "</pre>"}'


app.run()
