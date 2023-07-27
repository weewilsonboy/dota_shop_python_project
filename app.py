from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.dialects.postgresql import UUID
import uuid

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://wilson:password@localhost:5432/dota_db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from seed import seed
app.cli.add_command(seed)

from controllers.hero_controller import hero_blueprint

app.register_blueprint(hero_blueprint)