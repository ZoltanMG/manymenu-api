from flask import Flask, jsonify, request
from pprint import pprint
from .modules.save_recipes import save_recipes
app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def hello_world():
    return jsonify({"hola": "mundo"})


@app.route("/reseta", methods=['POST'], strict_slashes=False)
def resetas():
    if request.method == "POST":
        print(save_recipes(request.json))
        return jsonify(
            {"state": "ok"}
        ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
