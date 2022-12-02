from pydantic import BaseModel


class FailVerifyResponse(BaseModel):
    resp_: str = "034"
    resp_msg: bool = False


class SucessVerifyResponse(BaseModel):
    resp_: str = "000"
    resp_msg: bool = True
