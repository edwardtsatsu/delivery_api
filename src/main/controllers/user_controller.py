from flask import Blueprint
from flask_pydantic import validate

from src.main.requests.signup_request import SignupRequest
from src.main.requests.verify_otp_request import VerifyOtpRequest
from src.main.services.user_service import save_new_user, otp_verification

user_signup_blueprint = Blueprint("signup", "__name__")
verify_otp_blueprint = Blueprint("verify-otp", "__name__")


@user_signup_blueprint.route("/user/signup", methods=["POST"])
@validate()
def save_user(body: SignupRequest):
    return save_new_user(body)


@verify_otp_blueprint.route("user/verify-otp", methods=['POST'])
@validate()
def verify_otp(body: VerifyOtpRequest):
    return otp_verification(body)