from datetime import datetime

from sqlalchemy import desc, select

from src.extensions import db
from src.main.requests.signup_request import SignupRequest
from src.main.requests.verify_otp_request import VerifyOtpRequest
from src.main.responses.signup_response import (
    AccountCreatedResponse,
    AcoountNotCreatedResponse,
    UserExistResponse,
)

from ..models.otp_code_model import OtpCode
from ..models.user_model import Role, User


def save_new_user(body: SignupRequest):
    if body.user_type == "user":
        res = Role.query.filter_by(role_name="user").first()

    else:
        res = Role.query.filter_by(role_name="rider").first()

    user = bool(User.query.filter_by(email=body.email).first())

    if user:
        return AcoountNotCreatedResponse(), 409

    user = bool(User.query.filter_by(phone_number=body.phone_number).first())

    if user:
        return AcoountNotCreatedResponse(), 409

    if not user:
        new_user = User(
            email=body.email,
            phone_number=body.phone_number,
            username=body.username,
            password=body.password,
        )
        db.session.add(new_user)
        new_user.roles.append(res)
        db.session.commit()
        AccountCreatedResponse(), 200
    else:
        UserExistResponse(), 405

    return UserExistResponse(), 405


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


def save_changes(data: User) -> None:
    db.session.add(data)
    db.session.commit()
