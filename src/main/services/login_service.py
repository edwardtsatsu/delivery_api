import flask_bcrypt
from flask_jwt_extended import create_access_token

from src.extensions import db
from src.main.requests.login_request import LoginRequest

from ..models.user_model import User


def login(body: LoginRequest):
    email = body.email
    us_password = body.password.encode()

    user = User.query.filter_by(email=email).first()
    if not user:
        return "User Not Found", 404

    if flask_bcrypt.check_password_hash(user.password, us_password):
        acces_token = create_access_token(identity={"email": email})
        return {"access_token": acces_token}, 200
    else:
        return "Invalid Login Info", 400
