import os
from datetime import datetime
from random import randint

import requests
from dotenv import load_dotenv

load_dotenv()

from src.extensions import db
from src.main.requests.generate_otp_request import GenerateOtpRequest
from src.main.responses.generate_otp_response import GenerateOtpResponse, OtpErrorResponse

from ..models.otp_code_model import OtpCode


def generate_otp(body: GenerateOtpRequest):
    otp_code = randint(1000, 9999)
    payload = sms_payload(otp_code, body)

    response = requests.post(url=os.getenv("SMS_URL"), json=payload)

    # if sent the succesfuly, save code in db
    if response.json()["responseCode"] == 200:
        otp = OtpCode(
            code=otp_code,
            phone_number=body.phone_number,
            generated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )
        save_otp_code(otp)
        return GenerateOtpResponse()
    else:
        return OtpErrorResponse()


def sms_payload(otp, body):
    return {
        "username": os.getenv("USER_NAME"),
        "password": os.getenv("PASSWORD"),
        "senderId": os.getenv("SENDER_ID"),
        "messageType": int(os.getenv("MESSAGE_TYPE")),
        "msisdn": body.phone_number,
        "message": os.getenv("MESSAGE") + str(otp),
    }


def save_otp_code(otp_obj):
    db.session.add(otp_obj)
    db.session.commit()
