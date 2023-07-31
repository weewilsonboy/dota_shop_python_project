from app import db
from models.courier import Courier
from models.hero import Hero
from models.item import Item
import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext
def seed():
    Courier.query.delete()
    Hero.query.delete()
    Item.query.delete()



    hero1 = Hero(name="Axe", gold= 2000)
    hero2 = Hero(name="Ancient Apparition",gold= 500)
    hero3 = Hero(name="Bounty Hunter", gold= 42000)
    item1 = Item(name="Tango", image_locator="/static/images/tango.png", cost=90)
    item2 = Item(name="Salve", image_locator="/static/images/salve.png", cost=110)
    item3 = Item(name="Clarity", image_locator="/static/clarity.png", cost=50)
    item4 = Item(name="Dust of Appearance", image_locator="/static/dust.png", cost=80)
    item5 = Item(name="Enchanted Mango", image_locator="/static/mango.png", cost=65)
    item6 = Item(name="Bottle", image_locator="/static/bottle.png", cost=675)
    item7 = Item(name="Observer Ward", image_locator="/static/obs.png", cost=0)
    item8 = Item(name="Sentry Ward", image_locator="/static/sentry.png", cost=50)
    item9 = Item(name="Smoke of Deceit", image_locator="/static/smoke.png", cost=50)
    item10 = Item(name="Town Portal Scroll", image_locator="/static/tp.png", cost=100)
    item11 = Item(name="Faerie Fire", image_locator="/static/faerie.png", cost=65)
    item12 = Item(name="Blood Grenade", image_locator="/static/blood_grenade.png", cost=65)
    item13 = Item(name="Aghanim's Shard", image_locator="/static/shard.png", cost=1400)


    db.session.add(hero1)
    db.session.add(hero2)
    db.session.add(hero3)

    db.session.add(item1)
    db.session.add(item2)
    db.session.add(item3)
    db.session.add(item4)
    db.session.add(item5)
    db.session.add(item6)
    db.session.add(item7)
    db.session.add(item8)
    db.session.add(item9)
    db.session.add(item10)
    db.session.add(item11)
    db.session.add(item12)
    db.session.add(item13)

    db.session.commit()

    courier1 = Courier(hero_id=hero1.id, item_id=item1.id)

    db.session.add(courier1)

    db.session.commit()