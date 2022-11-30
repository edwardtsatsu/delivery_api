import os

from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from .main.models import otp_code_model, user_model

from .main.controllers.signup_controller import user_signup_blueprint
from .main.controllers.verify_otp_controller import verify_otp_blueprint
from .main.controllers.generate_otp_controller import generate_otp_blueprint
from .extensions import db, migrate


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(user_signup_blueprint, url_prefix="/api/v1")
    app.register_blueprint(verify_otp_blueprint, url_prefix="/api/v1")
    app.register_blueprint(generate_otp_blueprint,  url_prefix="/api/v1")
    return app
