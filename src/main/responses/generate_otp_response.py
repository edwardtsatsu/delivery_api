from pydantic import BaseModel


class GenerateOtpResponse(BaseModel):
    resp_code: str = "000"
    resp_desc: str = "OTP has been sent to customers phonenumber"
