from pydantic import BaseModel


class VerifyPhoneNumberRequest(BaseModel):
    phone_number: str
