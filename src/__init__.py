import os

from dotenv import load_dotenv

load_dotenv()
from flask import Flask
from flask_jwt_extended import JWTManager

from .extensions import db, migrate
from .main.controllers.forget_password_controlller import reset_password_blueprint
from .main.controllers.generate_otp_controller import generate_otp_blueprint
from .main.controllers.login_controller import (
    create_order_blueprint,
    user_login_blueprint,
)
from .main.controllers.signup_controller import user_signup_blueprint
from .main.controllers.verify_otp_controller import verify_otp_blueprint
from .main.models import otp_code_model, user_model


def create_app():
    app = Flask(__name__)
    JWTManager(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY_JWT")

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(user_signup_blueprint, url_prefix="/api/v1")
    app.register_blueprint(verify_otp_blueprint, url_prefix="/api/v1")
    app.register_blueprint(generate_otp_blueprint, url_prefix="/api/v1")
    app.register_blueprint(user_login_blueprint, url_prefix="/api/v1")
    app.register_blueprint(create_order_blueprint, url_prefix="/api/v1")
    app.register_blueprint(reset_password_blueprint, url_prefix="/api/v1")

    return app
