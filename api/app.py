from flask import Flask, jsonify, request
from models import storage
from models.recipe import Recipe
from models import storage

app = Flask(__name__)

@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    return storage.get_all(response=True)


@app.route("/reseta", methods=['POST', 'DELETE'], strict_slashes=False)
def resetas():
    if request.method == "POST":
        res_recipe = request.json
        new_recipe = Recipe(
            recipe_name=res_recipe['recipe_name'],
            ingredients=res_recipe['ingredients']
            )
        new_recipe.save()
        return jsonify(new_recipe.__dict__), 200
    if request.method == "DELETE":
        print("delete:", request.json)

        recipe = storage.get(request.json['id'])
        recipe.delete()
        return jsonify({"delete":"Ok"}), 203

@app.after_request
def after(response):
    """
    Esta función verifica la sesión después de una solicitud y
    le da al CORS con la interfaz que permite la conexión
    entre la parte posterior y la frontal.
    """
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
