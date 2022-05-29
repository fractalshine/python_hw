from utils import *
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    candidate_dicts = load_candidates_from_json()
    return render_template('index.html', candidates=candidate_dicts)


@app.route("/skills/<skill>")
def search_skills(skill):
    candidate_dicts = get_candidates_by_skill(skill)
    skilled_count = len(candidate_dicts)
    return render_template('skills.html', skilled=candidate_dicts, count=skilled_count)


@app.route("/search/<name>")
def search_names(name):
    candidate_dicts = get_candidates_by_name(name)
    skilled_count = len(candidate_dicts)
    return render_template('search.html', skilled=candidate_dicts, count=skilled_count)


@app.route("/candidate/<int:pk>")
def page_uid(pk):
    candidate_dict = get_candidate(pk)
    return render_template('card.html', candidate=candidate_dict)


app.run()
