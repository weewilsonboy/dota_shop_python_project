from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.courier import Courier
from models.hero import Hero
from models.item import Item
from app import db

order_blueprint = Blueprint("order", __name__)


@order_blueprint.route('/order')
def order_page():
    couriers = Courier.query.all()
    
    return render_template('/order/index.jinja', couriers = couriers)

@order_blueprint.route('/order', methods=["POST"])
def order_confirm():
    hero_name = request.form['hero_name']
    order_hero = Hero.query.filter_by(name = hero_name).first()
    item_name = request.form['item_name']
    order_item = Item.query.filter_by(name = item_name).first()
    courier = Courier(hero_id = order_hero.id, item_id = order_item.id)
    db.session.add(courier)
    db.session.commit()

    return redirect('/order')



@order_blueprint.route('/order/new')
def new_order():
    return render_template('/order/new.jinja', heroes = Hero.query.all(), items = Item.query.all())