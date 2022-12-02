from src.main.requests.forget_password_request import ForgetPasswordRequest
from src.main.responses.forget_password_response import ForgetPasswordResponse


class ForgetPassword:
    def __init__(self, body: ForgetPasswordRequest) -> None:
        self.phone_number = body

    def reset_password(self):
        return "oaky"