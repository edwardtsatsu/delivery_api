from pydantic import BaseModel


class ResetPasswordRequest(BaseModel):
    phone_number: str
    new_password: str
