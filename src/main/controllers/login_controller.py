from flask import Blueprint
from flask_pydantic import validate

from src.main.requests.login_request import LoginRequest
from src.main.services.login_service import login

user_login_blueprint = Blueprint("user-login", "__name__")


@user_login_blueprint.route("/user/login", methods=["POST"])
@validate()
def user_login(body: LoginRequest):
    return login(body)
