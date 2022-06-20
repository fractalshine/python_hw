from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/search')
def search_page():
    s = request.args['s']
    return f'Вы ввели слово {s}'


@app.route('/filter')
def filter_page():
    from_value = request.args['from']
    to_value = request.args['to']
    return f'Ищем в диапазоне от {from_value} до {to_value}'


@app.route('/newsearch')
def new_search_page():
    s = request.args.get('s')
    if s:
        return f'Вы ввели слово {s}'
    # else
    return 'Вы не ввели ничего'


app.run()
