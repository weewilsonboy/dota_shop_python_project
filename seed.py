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



    hero4 = Hero(name="Abaddon", gold= 750)
    hero5 = Hero(name="Alchemist", gold= 5500)
    hero2 = Hero(name="Ancient Apparition",gold= 500)
    hero6 = Hero(name="Anti-Mage", gold= 5000)
    hero7 = Hero(name="Arc Warden", gold= 2222)
    hero1 = Hero(name="Axe", gold= 2000)
    hero8 = Hero(name="Bane", gold= 700)
    hero9 = Hero(name="Batrider", gold= 700)
    hero10 = Hero(name="Beastmaster", gold= 650)
    hero11 = Hero(name="Bloodseeker", gold= 125)
    hero3 = Hero(name="Bounty Hunter", gold= 42000)
    hero12 = Hero(name="Brewmaster", gold= 750)
    hero13 = Hero(name="Bristleback", gold= 870)
    hero14 = Hero(name="Broodmother", gold= 640)
    hero15 = Hero(name="Centaur Warrunner", gold= 550)
    hero16 = Hero(name="Chaos Knight", gold= 6000)
    hero17 = Hero(name="Chen", gold= 80)
    hero18 = Hero(name="Clinkz", gold= 1500)
    hero19 = Hero(name="Clockwerk", gold= 3200)
    hero20 = Hero(name="Crystal Maiden", gold= 1200)
    hero21 = Hero(name="Dark Seer", gold= 466)
    hero22 = Hero(name="Dark Willow", gold= 800)
    hero23 = Hero(name="Dawnbreaker", gold= 1200)
    hero24 = Hero(name="Dazzle", gold= 600)
    hero25 = Hero(name="Death Prophet", gold= 800)
    hero26 = Hero(name="Disruptor", gold= 45)
    hero27 = Hero(name="Doom", gold= 666)
    hero28 = Hero(name="Dragon Knight", gold= 1001)
    hero29 = Hero(name="Drow Ranger", gold= 3111)
    hero30 = Hero(name="Earth Spirit", gold= 100)
    hero31 = Hero(name="Earthshaker", gold= 4200)
    hero32 = Hero(name="Elder Titan", gold= 200)
    hero33 = Hero(name="Ember Spirit", gold= 1998)
    hero34 = Hero(name="Enchantress", gold= 120)
    hero35 = Hero(name="Enigma", gold= 99)
    hero36 = Hero(name="Faceless Void", gold= 1600)
    hero37 = Hero(name="Grimstroke", gold= 522)
    hero38 = Hero(name="Gyrocopter", gold= 100)
    hero39 = Hero(name="Hoodwink", gold= 322)


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
    db.session.add(hero4)
    db.session.add(hero5)
    db.session.add(hero6)
    db.session.add(hero7)
    db.session.add(hero8)
    db.session.add(hero9)
    db.session.add(hero10)
    db.session.add(hero11)
    db.session.add(hero12)
    db.session.add(hero13)
    db.session.add(hero14)
    db.session.add(hero15)
    db.session.add(hero16)
    db.session.add(hero17)
    db.session.add(hero18)
    db.session.add(hero19)
    db.session.add(hero20)
    db.session.add(hero21)
    db.session.add(hero22)
    db.session.add(hero23)
    db.session.add(hero24)
    db.session.add(hero25)
    db.session.add(hero26)
    db.session.add(hero27)
    db.session.add(hero28)
    db.session.add(hero29)
    db.session.add(hero30)
    db.session.add(hero31)
    db.session.add(hero32)
    db.session.add(hero33)
    db.session.add(hero34)
    db.session.add(hero35)
    db.session.add(hero36)
    db.session.add(hero37)
    db.session.add(hero38)
    db.session.add(hero39)

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
    hero1.items_held +=1
    courier1 = Courier(hero_id=hero1.id, item_id=item1.id)

    db.session.add(courier1)

    db.session.commit()