from flask import Blueprint
from flask_pydantic import validate

from src.main.requests.verify_otp_request import VerifyOtpRequest
from src.main.services.verfiy_otp_service import otp_verification

verify_otp_blueprint = Blueprint("verify-otp", "__name__")


@verify_otp_blueprint.route("/user/verify-otp", methods=["POST"])
@validate()
def verify_otp(body: VerifyOtpRequest):
    return otp_verification(body)
