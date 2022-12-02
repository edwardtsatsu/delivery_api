from flask import Blueprint
from flask_pydantic import validate
from flask_jwt_extended import jwt_required
from src.main.requests.login_request import LoginRequest
from src.main.services.login_service import login, make_order

user_login_blueprint = Blueprint("user-login", "__name__")
create_order_blueprint = Blueprint("user-create-order", "__name__")


@user_login_blueprint.route("/user/login", methods=["POST"])
@validate()
def user_login(body: LoginRequest):
    return login(body)


@create_order_blueprint.route("/user/create-order", methods=["POST"])
@jwt_required()
@validate()
def create_order(body: LoginRequest):
    return make_order(body)
