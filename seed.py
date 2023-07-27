from app import db
from models.courier import Courier
from models.hero import Hero
from models.item import Item
import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext
def seed():
    
    user1 = Hero(name="Axe", gold= 2000)
    user2 = Hero(name="Ancient Apparition",gold= 500)
    user3 = Hero(name="Bounty Hunter", gold= 42000)
    location1 = Item(image_locator="/static/images/tango.png", cost=90)
    location2 = Item(image_locator="/satic/images/salve.png", cost=110)

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)

    db.session.add(location1)
    db.session.add(location2)
    db.session.commit()