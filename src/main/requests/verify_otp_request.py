from pydantic import BaseModel


class VerifyOtpRequest(BaseModel):
    code: str
    phone_number: str
