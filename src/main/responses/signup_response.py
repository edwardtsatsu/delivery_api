from pydantic import BaseModel


class SignupResponse(BaseModel):
    resp_code: int = 200
    resp_desc: str
