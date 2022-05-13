from utils import load_candidates
from flask import Flask

app = Flask(__name__)

candidates_list = load_candidates()


@app.route("/")
def page_index():
    string = ""
    for dictionary in candidates_list:
        string += "Имя кандидата - " + dictionary['name'] + "\n" + \
                  "Позиция кандидата - " + dictionary['position'] + "\n" + \
                  "Навыки через запятую: " + dictionary['skills'] + "\n" + \
                  "" + "\n"
    return f'{"<pre>" + string + "</pre>"}'


@app.route("/candidates/<int:uid>")
def page_uid(uid):
    string = ""
    pic = ""
    for dictionary in candidates_list:
        if uid == dictionary['id']:
            string += "Имя кандидата - " + dictionary['name'] + "\n" + \
                      "Позиция кандидата - " + dictionary['position'] + "\n" + \
                      "Навыки через запятую: " + dictionary['skills'] + "\n" + \
                      "" + "\n"
            pic = dictionary['picture']
    return f'<img src="{pic}">' \
           f'{"<pre>" + string + "</pre>"}'


@app.route("/skills/<skill>")
def page_skills(skill):
    string = ""
    for dictionary in candidates_list:
        string_lower = dictionary['skills'].lower()
        skills_list = string_lower.split(", ")
        if skill.lower() in skills_list:
            string += "Имя кандидата - " + dictionary['name'] + "\n" + \
                      "Позиция кандидата - " + dictionary['position'] + "\n" + \
                      "Навыки через запятую: " + dictionary['skills'] + "\n" + \
                      "" + "\n"
    return f'{"<pre>" + string + "</pre>"}'


app.run()
