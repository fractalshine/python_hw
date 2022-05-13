from flask import Flask

app = Flask(__name__)


@app.route("/")
def page_index():
    return "Главная страничка"


@app.route("/profile/")
def page_profile():
    return "Профиль пользователя"


@app.route("/num/")
def page_num():
    return 1


@app.route('/users/<int:uid>')
def profile(uid):
    print(uid)
    print(type(uid))

    return f"страница пользователя {uid}"


letters = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", }


@app.route('/get_letter/<int:index>')
def page_letter(index):
    letter = letters.get(index)
    return letter


app.run()
