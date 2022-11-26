import os

from dotenv import load_dotenv
load_dotenv()
from flask import Flask

from .controllers.user_controller import user_signup_blueprint
from .extensions import db, migrate


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(user_signup_blueprint, url_prefix="/api/v1")

    return app