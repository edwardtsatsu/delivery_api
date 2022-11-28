from random import randint
from datetime import datetime
from src.extensions import db
from src.main.requests.signup_request import SignupRequest
from src.main.requests.verify_otp_request import VerifyOtpRequest

from ..models.otp_code_model import OtpCode
from ..models.user_model import Role, User


def save_new_user(body: SignupRequest):
    if body.user_type == "user":
        res = Role.query.filter_by(role_name="user").first()
    else:
        res = Role.query.filter_by(role_name="rider").first()

    user = bool(User.query.filter_by(email=body.email).first())

    if user:
        return {
            "resp_code": "001",
            "resp_msg": "account no created with these details.",
        }, 409

    user = bool(User.query.filter_by(phone_number=body.phone_number).first())

    if user:
        return {
            "resp_code": "001",
            "resp_msg": "account no created with these details.",
        }, 409

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

        # generate otp and save to db
        resp = User.query.filter_by(email=body.email).first()
        otp = OtpCode(code=randint(1000, 9999), user_id=resp.id)
        db.session.add(otp)
        db.session.commit()

        # call sms service to send otp to customer number
        return {
            "resp_code": "000",
            "resp_msg": "otp has been sent to customers phone number",
        }
    else:
        response_object = {
            "resp_code": "001",
            "resp_msg": "User already exists.",
        }
    return response_object, 409


def otp_verification(body: VerifyOtpRequest):
    user = bool(User.query.filter_by(phone_number=body.phone_number).first())
    if not user:
        return {
            "resp_code": "001",
            "resp_msg": "User with this phone_number not found.",
        }, 404
    id = User.query.filter_by(phone_number=body.phone_number).first().id
    otp_resp = OtpCode.query.filter_by(user_id=id).first()
    if body.code == otp_resp.code:
        if otp_expiry(otp_resp.generated_at) > 5:
            return {
                "resp_code": "022",
                "resp_msg": "otp has expired.",
            }, 404
        OtpCode.query.filter_by(user_id=id).update({"verified": True})
        db.session.commit()
    else:
        return {
            "resp_code": "001",
            "resp_msg": "Invalid otp",
        }, 403

    return {"resp_code": "000", "resp_msg": "successfully verified user and login!"}


def otp_expiry(generated_at):
    end_time = datetime.strptime(
        datetime.now().strftime("%Y-%m-%d" "%H:%M:%S"), "%Y-%m-%d" "%H:%M:%S"
    )
    min = (end_time - generated_at).seconds / 60
    print(min)
    return min


def save_changes(data: User) -> None:
    db.session.add(data)
    db.session.commit()
