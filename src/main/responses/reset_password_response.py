from pydantic import BaseModel


class SucessResponse(BaseModel):
    resp_code: str = "000"
    resp_msg: str = "Password has been reset successfully!"


class FailureResponse(BaseModel):
    resp_code: str = "045"
    resp_msg: str = "password is weak, password must have at least 8 characters!"
