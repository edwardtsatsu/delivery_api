from src.extensions import db
from src.main.models.user_model import User
from src.main.requests.verify_phone_number_request import VerifyPhoneNumberRequest
from src.main.responses.verify_phone_number_response import (
    FailVerifyResponse,
    SucessVerifyResponse,
)


class VerifyPhoneNumber:
    def __init__(self, body: VerifyPhoneNumberRequest):
        self.phone_number = body.phone_number

    def verify_phone_number(self):
        if bool(User.query.filter_by(phone_number=self.phone_number).first()):
            return SucessVerifyResponse(), 200
        else:
            return FailVerifyResponse(), 404
