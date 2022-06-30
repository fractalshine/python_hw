from flask import Flask, render_template
from books_dao import BooksDAO

app = Flask(__name__)
books_dao = BooksDAO()


@app.route("/")
def page_index():
    books = books_dao.get_all()
    return render_template("index.html", candidates=books)
