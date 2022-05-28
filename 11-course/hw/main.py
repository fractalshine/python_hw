from utils import *
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    candidate_dicts = load_candidates_from_json()
    return render_template('index.html', candidates=candidate_dicts)


@app.route("/skills/<skill>")
def page_skills(skill):
    return render_template('skills.html')
    pass


@app.route("/candidate/<int:pk>")
def page_uid(pk):
    candidate_dict = get_candidate(pk)
    return render_template('card.html', candidate=candidate_dict)


app.run()
