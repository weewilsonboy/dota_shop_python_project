from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(UUID(as_uuid = True), primary_key = True, default=uuid.uuid4)
    name = db.Column(db.String(64))
    image_locator = db.Column(db.String(64))
    cost = db.Column(db.Integer)
    description = db.Column(db.Text)
    couriers = db.relationship('Courier', backref='item')


    def __repr__(self):
        return f"{self.id} {self.image_locator} {self.cost}"