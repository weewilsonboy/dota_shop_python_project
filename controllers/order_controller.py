from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.courier import Courier

hero_blueprint = Blueprint("hero", __name__)


@hero_blueprint.route('/hero')
def hero_page():
    couriers = Courier.query.all()
    
    return render_template('/order/index.jinja', couriers = couriers)