from flask import Flask, jsonify, request
from models import storage
from models.recipe import Recipe
from models import storage

app = Flask(__name__)

@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    return storage.get_all()


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
        recipe = storage.get(request.json['id'])
        print("delete:", type(recipe))
        recipe.delete()
        return jsonify({"delete":"Ok"}), 203



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
