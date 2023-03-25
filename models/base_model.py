from uuid import uuid4
from models import storage

class Basemodel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def to_dict(self):
        tmp_dict = self.__dict__
        copy_dict = tmp_dict.copy()
        if "_sa_instance_state" in copy_dict:
            del copy_dict['_sa_instance_state']
        return copy_dict

    def save(self):
        storage.save(self)

    def delete(self):
        storage.delete(self)