from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.courier import Courier
from models.hero import Hero
from models.item import Item

hero_blueprint = Blueprint("hero", __name__)


@hero_blueprint.route('/hero')
def hero_page():
    heroes = Hero.query.all()
    
    return render_template('/hero/index.jinja', heroes = heroes)