from models.base_model import Basemodel

class Recipe(Basemodel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)