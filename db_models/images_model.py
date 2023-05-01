import uuid
from sqlalchemy import Column, DateTime, ForeignKey, String, LargeBinary

from database import db


class ImagesModel(db.Model):
    __tablename__ = 'images'

    id = Column(String(255), primary_key=True, nullable=False)
    name = Column(String(255), nullable=True)
    sketch_image = Column(LargeBinary)
    predicted_image = Column(LargeBinary)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

    user_id = Column(String(), ForeignKey("users.id"), nullable=False)

    def __init__(self, name, created_at, updated_at, user_id, sketch_image=None, predicted_image=None):
        self.id = str(uuid.uuid4().hex)
        self.name = name
        self.predicted_image = predicted_image
        self.sketch_image = sketch_image
        self.created_at = created_at
        self.updated_at = updated_at
        self.user_id = user_id

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
