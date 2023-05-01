import uuid

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from database import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = Column(String(255), primary_key=True, nullable=False)
    name = Column(String(255), nullable=True)
    password = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    images = relationship(
        "ImagesModel", backref="image", cascade="all, delete-orphan", lazy="dynamic"
    )

    def __init__(self, name, password, email=None):
        self.id = str(uuid.uuid4().hex)
        self.name = name
        self.password = password
        self.email = email

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "password": self.password,
            "email": self.email,
        }
