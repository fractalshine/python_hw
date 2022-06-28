from flask import Flask

from loader.views import loader_blueprint
from main.views import main_blueprint

# from functions import ...


app = Flask(__name__)
# Регистрируем блюпринты
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

if __name__ == "__main__":
    app.run(port=5008)
