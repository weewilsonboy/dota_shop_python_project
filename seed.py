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
    item1 = Item(name="Tango", image_locator="/static/images/tango.png", cost=90, description = "Forage to survive on the battlefield.")
    item2 = Item(name="Salve", image_locator="/static/images/salve.png", cost=110, description = "A magical salve that can quickly mend even the deepest of wounds.")
    item3 = Item(name="Clarity", image_locator="/static/images/clarity.png", cost=50, description = "Clear water that enhances the ability to meditate.")
    item4 = Item(name="Dust of Appearance", image_locator="/static/images/dust.png", cost=80, description = "One may hide visage, but never volume.")
    item5 = Item(name="Enchanted Mango", image_locator="/static/images/mango.png", cost=65, description = "The bittersweet flavors of Jidi Isle are irresistible to amphibians.")
    item6 = Item(name="Bottle", image_locator="/static/images/bottle.png", cost=675, description = "An old bottle that survived the ages, the contents placed inside become enchanted.")
    item7 = Item(name="Observer Ward", image_locator="/static/images/obs.png", cost=0, description = "A form of half-sentient plant, often cultivated by apprentice wizards.")
    item8 = Item(name="Sentry Ward", image_locator="/static/images/sentry.png", cost=50, description = "A form of plant originally grown in the garden of a fearful king.")
    item9 = Item(name="Smoke of Deceit", image_locator="/static/images/smoke.png", cost=50, description = "The charlatan wizard Myrddin's only true contribution to the arcane arts.")
    item10 = Item(name="Town Portal Scroll", image_locator="/static/images/tp.png", cost=100, description = "What a hero truly needs.")
    item11 = Item(name="Faerie Fire", image_locator="/static/images/faerie.png", cost=65, description = "The ethereal flames from the ever-burning ruins of Kindertree ignite across realities.")
    item12 = Item(name="Blood Grenade", image_locator="/static/images/blood_grenade.png", cost=65, description = "")
    item13 = Item(name="Aghanim's Shard", image_locator="/static/images/shard.png", cost=1400, description = "With origins known only to a single wizard, fragments of this impossible crystal are nearly as coveted as the renowned scepter itself.")


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