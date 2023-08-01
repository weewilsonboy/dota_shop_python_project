from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.courier import Courier
from models.hero import Hero
from models.item import Item
from app import db

hero_blueprint = Blueprint("hero", __name__)


@hero_blueprint.route('/hero')
def hero_page():
    heroes = Hero.query.order_by(Hero.name).all()
    couriers = Courier.query.all()
    return render_template('/hero/index.jinja', heroes = heroes, couriers = couriers)

@hero_blueprint.route('/sale/<id>')
def item_sale(id):
    
    courier_to_edit = Courier.query.get(id)
    item_being_sold = Item.query.get(courier_to_edit.item.id)
    hero_selling = Hero.query.get(courier_to_edit.hero.id)
    hero_selling.gold += (item_being_sold.cost//2)
    courier_to_edit.sold = True
    db.session.commit()
    return redirect('/hero')