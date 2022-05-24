from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def page_index():
    my_debt = 10  # my_debt = 0
    return render_template("hello-1.html", my_debt=my_debt)


app.run()
