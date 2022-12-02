from pydantic import BaseModel


class ForgetPasswordResponse(BaseModel):
    resp_code: str = "000"
    resp_msg: str = "Password has been reset successfully!"
