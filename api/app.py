from flask import Flask, jsonify, request
from models import storage
from models.recipe import Recipe
from models import storage

app = Flask(__name__)

@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    all_recipes_to_response = storage.get_all(response=True)
    return all_recipes_to_response

@app.route("/favorite", methods=['POST'], strict_slashes=False)
def favorite():
    recipe = storage.get(request.json['id'])
    recipe.favorite = request.json['favorite']
    recipe.save()
    return "ok"


@app.route("/reseta", methods=['POST', 'DELETE'], strict_slashes=False)
def reseta():
    if request.method == "POST":
        recipe_name = request.json['recipe_name']
        ingredients = request.json['ingredients']
        favorite = request.json['favorite']
        new_recipe = Recipe(
            recipe_name=recipe_name,
            ingredients=ingredients,
            favorite=favorite
            )
        new_recipe.save()
        return jsonify(new_recipe.__dict__), 200
    if request.method == "DELETE":
        recipe_to_delete = storage.get(request.json['id'])
        recipe_to_delete.delete()
        return jsonify({"delete":"Ok"}), 203

@app.after_request
def after(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
