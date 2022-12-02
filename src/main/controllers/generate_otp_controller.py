from flask import Blueprint
from flask_pydantic import validate

from src.main.requests.generate_otp_request import GenerateOtpRequest
from src.main.services.generated_otp_service import GenerateOtpService

generate_otp_blueprint = Blueprint("generate-otp", "__name__")


@generate_otp_blueprint.route("/user/generate-otp", methods=["POST"])
@validate()
def create_otp(body: GenerateOtpRequest):
    return GenerateOtpService(body.phone_number).generate_otp()
