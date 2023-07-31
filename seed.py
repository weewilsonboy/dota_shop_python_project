from app import db
from models.courier import Courier
from models.hero import Hero
from models.item import Item
import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext
def seed():
    Hero.query.delete()
    Item.query.delete()
    Courier.query.delete()



    hero1 = Hero(name="Axe", gold= 2000)
    hero2 = Hero(name="Ancient Apparition",gold= 500)
    hero3 = Hero(name="Bounty Hunter", gold= 42000)
    item1 = Item(name="Tango", image_locator="/static/images/tango.png", cost=90)
    item2 = Item(name="Salve", image_locator="/static/images/salve.png", cost=110)
    item3 = Item(name="Clarity", image_locator="/static/clarity.png", cost=50)


    db.session.add(hero1)
    db.session.add(hero2)
    db.session.add(hero3)

    db.session.add(item1)
    db.session.add(item2)

    db.session.commit()

    courier1 = Courier(hero_id=hero1.id, item_id=item1.id)

    db.session.add(courier1)

    db.session.commit()