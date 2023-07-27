from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Hero(db.Model):
    __tablename__ = "heroes"

    id = db.Column(UUID(as_uuid = True), primary_key = True, default=uuid.uuid4)
    name = db.Column(db.String(64))
    gold = db.Column(db.Integer)
    couriers = db.relationship('Courier', backref='hero')

    
    def __repr__(self):
        return f"{self.id} {self.gold}"