from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Courier(db.Model):
    __tablename__ = "couriers"

    id = db.Column(UUID(as_uuid = True), primary_key = True, default=uuid.uuid4)
    hero_id = db.Column(UUID(as_uuid = True), db.ForeignKey('heroes.id'))
    item_id = db.Column(UUID(as_uuid = True), db.ForeignKey('items.id'))
    sold = db.Column(db.Boolean, server_default = 'false')

    def __repr__(self):
        return f"{self.id} {self.hero_id} {self.item_id}"