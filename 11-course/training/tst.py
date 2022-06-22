from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', )
def page_index():
    page_content = """ 
    <p>Даниил Хармс</p>
    <p>В гостях</p>
    <br/>
    <p>
    Мышь меня на чашку чая<br>
    Пригласила в новый дом.<br>
    Долго в дом не мог войти я,<br>
    Всё же влез в него с трудом.
    </p>
    <input type="text" value="текст вводить тут">
    <input type="text" name="phone">
    <form action="http://httpbin.org/get">
    <input type="text" name="phone">
    <input type="submit">
    </form>
    """
    return page_content


app.run()
