import flask_bcrypt
from flask_jwt_extended import create_access_token, get_jwt_identity

from src.extensions import db
from src.main.requests.login_request import LoginRequest

from ..models.user_model import User


def login(body: LoginRequest):
    email = body.email
    password = body.password.encode()
    

    user = User.query.filter_by(email=email).first()
    if not user:
        return "User Not Found", 404

    if flask_bcrypt.check_password_hash(user.password, password):
        acces_token = create_access_token(identity=user.id)
        return {"access_token": acces_token, "user_id": user.id}, 200
    else:
        return {'resp_code': '003', 'resp_msg':"Invalid Login Info"}, 400


def make_order(body: LoginRequest):
    # Access the identity of the current user with get_jwt_identity
    print(body.email, body.password)
    current_user = get_jwt_identity()
    return {"logged_in_as": current_user}, 200
