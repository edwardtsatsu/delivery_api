from src.extensions import db
from src.main.requests.reset_password_request import ResetPasswordRequest
from src.main.responses.reset_password_response import FailureResponse, SucessResponse
from src.main.services.signup_service import password_encoder

from ..models.user_model import User


class ResetPassword:
    def __init__(self, body: ResetPasswordRequest) -> None:
        self.phone_number = body.phone_number
        self.new_password = body.new_password

    def reset_password(self):
        # check the length of password and validate it if good
        User.query.filter_by(phone_number=self.phone_number).update(
            {User.password: password_encoder(self.new_password)}
        )
        db.session.commit()
        return SucessResponse(), 200
