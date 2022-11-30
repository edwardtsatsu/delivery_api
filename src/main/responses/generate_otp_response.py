from pydantic import BaseModel


class GenerateOtpResponse(BaseModel):
    resp_code: str = "000"
    resp_desc: str = "OTP has been sent to customers phonenumber"


class OtpErrorResponse(BaseModel):
    resp_code: str = "012"
    resp_desc: str = "could not send otp, click on resend"
