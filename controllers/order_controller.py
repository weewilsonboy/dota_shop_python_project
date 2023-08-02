from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.courier import Courier
from models.hero import Hero
from models.item import Item
from app import db

order_blueprint = Blueprint("order", __name__)


@order_blueprint.route('/')
def homepage():
    couriers = Courier.query.all()
    
    return render_template('/index.jinja', couriers = couriers)

@order_blueprint.route('/order')
def order_page():
    couriers = Courier.query.all()
    
    return render_template('/order/index.jinja', couriers = couriers, error_msg = "")
@order_blueprint.route('/order', methods=["POST"])
def order_confirm():
    number = int(request.form['number'])
    hero_name = request.form['hero_name']
    order_hero = Hero.query.filter_by(name = hero_name).first()
    item_name = request.form['item_name']
    order_item = Item.query.filter_by(name = item_name).first()

    if number + order_hero.items_held > 9:
        return render_template('/order/index.jinja', couriers = Courier.query.all(), error_msg = f"Not enough inventory space for {hero_name} to buy {number} {item_name}(s)")




    if order_item.cost * number > order_hero.gold:
        return render_template('/order/index.jinja', couriers = Courier.query.all(), error_msg = f"Not enough gold for {hero_name} to buy {number} {item_name}(s)")
    order_hero.gold -= order_item.cost

    
    
    while number > 0:
        order_hero.items_held += 1
        courier = Courier(hero_id = order_hero.id, item_id = order_item.id)
        db.session.add(courier)
        number -= 1
    db.session.commit()

    return redirect('/order')



@order_blueprint.route('/order/new')
def new_order():
    return render_template('/order/new.jinja', heroes = Hero.query.order_by(Hero.name).all(), items = Item.query.all())