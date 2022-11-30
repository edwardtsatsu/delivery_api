from pydantic import BaseModel


class GenerateOtpRequest(BaseModel):
    phone_number: str
