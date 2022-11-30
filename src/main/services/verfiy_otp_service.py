from datetime import datetime

from sqlalchemy import desc

from src.extensions import db
from src.main.models.otp_code_model import OtpCode
from src.main.requests.verify_otp_request import VerifyOtpRequest
from src.main.responses.signup_response import (
    AccountCreatedResponse,
    AcoountNotCreatedResponse,
    UserExistResponse,
)


def otp_verification(body: VerifyOtpRequest):
    user = bool(OtpCode.query.filter_by(phone_number=body.phone_number).first())
    if not user:
        return {
            "resp_code": "001",
            "resp_msg": "Invalid details",
        }, 404

    query = (
        OtpCode.query.filter_by(phone_number=body.phone_number)
        .order_by(desc(OtpCode.generated_at))
        .first()
    )

    if body.code == query.code and otp_expiry(query.generated_at) < 2:
        OtpCode.query.filter_by(phone_number=body.phone_number).update(
            {"verified": True}
        )
        db.session.commit()
        return {"resp_code": "000", "resp_msg": "successfully verified user and login!"}

    if otp_expiry(query.generated_at) > 2:
        return {"resp_code": "001", "resp_msg": "otp has expired!"}, 403

    return {
        "resp_code": "001",
        "resp_msg": "Invalid otp",
    }, 403


def otp_expiry(generated_at):
    end_time = datetime.strptime(
        datetime.now().strftime("%Y-%m-%d" "%H:%M:%S"), "%Y-%m-%d" "%H:%M:%S"
    )
    min = (end_time - generated_at).seconds / 60
    return min
