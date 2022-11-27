from datetime import datetime
from random import randint
import requests
from src.extensions import db
from src.main.requests.signup_request import SignupRequest

from ..models.otp_code_model import OtpCode
from ..models.user_model import Role, User


def save_new_user(body: SignupRequest):
    print(body.email, body.phone_number, body.username, body.password, body.user_type)
    if body.user_type == "user":
        res = Role.query.filter_by(role_name="user").first()
    else:
        res = Role.query.filter_by(role_name="rider").first()

    user = bool(User.query.filter_by(email=body.email).first())

    if user:
        return {
            "resp_code": "001",
            "resp_msg": "User with this email already exists.",
        }, 409

    user = bool(User.query.filter_by(phone_number=body.phone_number).first())

    if user:
        return {
            "resp_code": "001",
            "resp_msg": "User with this phone_number already exists.",
        }, 409

    if not user:
        new_user = User(
            email=body.email,
            phone_number=body.phone_number,
            username=body.username,
            password=body.password
        )

        db.session.add(new_user)
        new_user.roles.append(res)
        db.session.commit()
        
        resp = User.query.filter_by(email=body.email).first()
        save_otp = OtpCode(
        code=randint(1000, 9999),
        user_id=resp.id)
        db.session.add(save_otp)
        db.session.commit()
        
        # call send otp service to send otp to customer number
        return {
            "resp_code": '000',
            'resp_msg': 'otp has been sent to customers phone number'
        }
    else:
        response_object = {
            "resp_code": "001",
            "resp_msg": "User already exists.",
        }
    return response_object, 409

def get_all_users():
    return User.query.all()


def get_a_user(id):
    return User.query.filter_by(id=id).first()


def generate_token(user: User):
    try:
        auth_token = User.encode_auth_token(user.id)
        response_object = {
            "status": "success",
            "message": "Successfully registred.",
            "Authorization": auth_token.decode(),
        }, 201
    except Exception as e:
        response_object = {
            "status": "fail",
            "message": f"Some error occurred. Please try again {e}",
        }, 422
        return response_object


def save_changes(data: User) -> None:
    db.session.add(data)
    db.session.commit()
