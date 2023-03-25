import json

class DBStorage:
    all_recipes = {}

    def load(self):
        from models.recipe import Recipe
        file_name = 'db_recipes.txt'
        with open(file_name, "r",  encoding="utf-8") as file:
            data_file = file.read()
            if data_file != "":
                recipes = json.loads(data_file)
        
        for recipe in recipes.items():
            self.all_recipes[recipe[1]['id']] = self.all_recipes.get(recipe[1]['id'], Recipe(
            recipe_name=recipe[1]['recipe_name'],
            ingredients=recipe[1]['ingredients'],
            id=recipe[1]['id']
            ))        
    
    def save(self, object):
        self.all_recipes[object.id] = object
        request_to_string = json.dumps(self.get_all())
        file_name = 'db_recipes.txt'
        with open(file_name,"w",  encoding="utf-8") as file:
            file.write(request_to_string)

    def delete(self, object):
        if object.id in self.all_recipes:
            del self.all_recipes[object.id]
            request_to_string = json.dumps(self.get_all())
            file_name = 'db_recipes.txt'
            with open(file_name,"w",  encoding="utf-8") as file:
                file.write(request_to_string)
    
    def get_all(self):
        recipes = {}
        for recipe in self.all_recipes.values():
            recipes[recipe.id] = recipe.__dict__
        return recipes
    
    def get(self, id):
        recipe = None
        for recipe in self.all_recipes.values():
            if recipe.id == id:
                return recipe
