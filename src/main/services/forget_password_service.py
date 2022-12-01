from src.main.requests.forget_password_request import ForgetPasswordRequest
from src.main.responses.forget_password_response import ForgetPasswordResponse


class ForgetPassword:
    def __init__(self, body: ForgetPasswordRequest) -> None:
        self.body = body.phone_number

    def reset_password(self):
        print(self.body)
        return ForgetPasswordResponse(), 200
