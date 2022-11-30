from datetime import datetime

from sqlalchemy import desc, select

from src.extensions import db
from src.main.requests.signup_request import SignupRequest
from src.main.requests.verify_otp_request import VerifyOtpRequest
from src.main.responses.signup_response import (AccountCreatedResponse,
                                                AcoountNotCreatedResponse,
                                                UserExistResponse)

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
