from flask import Blueprint
from flask_pydantic import validate

from src.main.requests.reset_password_request import ResetPasswordRequest
from src.main.services.reset_password_service import ResetPassword

reset_password_blueprint = Blueprint("reset-password", "__name__")


@reset_password_blueprint.route("/user/reset-password", methods=["POST"])
@validate()
def forget_password(body: ResetPasswordRequest):
    return ResetPassword(body).reset_password()
