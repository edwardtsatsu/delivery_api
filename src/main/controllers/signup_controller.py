from flask import Blueprint
from flask_pydantic import validate

from src.main.requests.signup_request import SignupRequest
from src.main.services.signup_service import save_new_user

user_signup_blueprint = Blueprint("signup", "__name__")


@user_signup_blueprint.route("/user/signup", methods=["POST"])
@validate()
def save_user(body: SignupRequest):
    return save_new_user(body)
