from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.item import Item
from app import db

item_blueprint = Blueprint("item", __name__)

@item_blueprint.route('/items')
def items():
    return render_template('/item/index.jinja', items = Item.query.order_by(Item.cost).all())

@item_blueprint.route('/items/<id>')
def individual_item(id):
    found_item = Item.query.get(id)
    return render_template('/item/individual.jinja', item=found_item)