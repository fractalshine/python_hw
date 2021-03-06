from flask import Flask
from app_config import Config
from loader.views import loader_blueprint
from main.views import main_blueprint

# from functions import ...


app = Flask(__name__)
app.config.from_object(Config)
# Регистрируем блюпринты
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


if __name__ == "__main__":
    app.run(port=5008)
