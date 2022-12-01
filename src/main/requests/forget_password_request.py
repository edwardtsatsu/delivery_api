from pydantic import BaseModel


class ForgetPasswordRequest(BaseModel):
    phone_number: str
