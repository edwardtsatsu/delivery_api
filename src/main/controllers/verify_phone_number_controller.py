from flask import Blueprint
from flask_pydantic import validate

from src.main.requests.verify_phone_number_request import VerifyPhoneNumberRequest
from src.main.services.verify_phone_number import VerifyPhoneNumber

verify_phone_number_blueprint = Blueprint("verify-phone-number", "__name__")


@verify_phone_number_blueprint.route("/user/verify-phone-number", methods=["POST"])
@validate()
def forget_password(body: VerifyPhoneNumberRequest):
    return VerifyPhoneNumber(body).verify_phone_number()
