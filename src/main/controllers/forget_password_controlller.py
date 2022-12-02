from flask import Blueprint
from flask_pydantic import validate

from src.main.requests.forget_password_request import ForgetPasswordRequest
from src.main.services.forget_password_service import ForgetPassword

reset_password_blueprint = Blueprint("reset-password", "__name__")


@reset_password_blueprint.route("/user/reset-password", methods=["POST"])
@validate()
def forget_password(body: ForgetPasswordRequest):
    return ForgetPassword(body.phone_number).reset_password()
