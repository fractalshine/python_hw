from flask import Flask, jsonify, request

app = Flask(__name__)
# Чтобы заработала кириллица
app.config['JSON_AS_ASCII'] = False


@app.route("/", methods=["POST"])
def demo_json():
    data = request.json
    print(data)
    return jsonify("Данные записаны")


app.run()
