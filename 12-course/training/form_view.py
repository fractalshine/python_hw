from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('my-form.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    with open("data.txt", "w", encoding="utf-8") as file:
        file.write(processed_text)
    return processed_text


app.run()
