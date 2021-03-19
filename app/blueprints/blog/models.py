from app import db
from datetime import datetime

class Post(db.Model):

    def __init__(self, name, price, image, description):
        self.name = name
        self.price = price
        self.image = image
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "image": self.image,
            "description": self.description,
            "created_on": self.created_on
        }