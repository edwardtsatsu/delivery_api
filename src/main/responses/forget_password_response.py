from pydantic import BaseModel


class ForgetPasswordResponse(BaseModel):
    resp_msg: str = "000"
    resp_msg: str = "Password has been reset successfully!"
