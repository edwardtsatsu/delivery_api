from datetime import datetime
from random import randint

from src.extensions import db
from src.main.requests.generate_otp_request import GenerateOtpRequest
from src.main.responses.generate_otp_response import GenerateOtpResponse

from ..models.otp_code_model import OtpCode


def generate_otp(body: GenerateOtpRequest):
    otp = OtpCode(
        code=randint(1000, 9999),
        phone_number=body.phone_number,
        generated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )
    save_otp_code(otp)
    # call the sms enpoint to send sms to the number provided
    return GenerateOtpResponse()


def save_otp_code(otp_obj):
    db.session.add(otp_obj)
    db.session.commit()
