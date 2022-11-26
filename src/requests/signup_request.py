from pydantic import BaseModel


class SignupRequest(BaseModel):
    email: str
    phone_number: str
    username: str
    password: str
    user_type: str
