from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.courier import Courier

order_blueprint = Blueprint("order", __name__)


@order_blueprint.route('/order')
def order_page():
    couriers = Courier.query.all()
    
    return render_template('/order/index.jinja', couriers = couriers)