import os
from datetime import datetime
from random import randint

import requests
from dotenv import load_dotenv

load_dotenv()

from src.extensions import db
from src.main.responses.generate_otp_response import (
    GenerateOtpResponse,
    OtpErrorResponse,
)

from ..models.otp_code_model import OtpCode


class GenerateOtpService:
    def __init__(self, body):
        self.phone_number = body.phone_number

    def generate_otp(self):
        self.otp_code = randint(1000, 9999)
        payload = self.sms_payload()

        response = requests.post(url=os.getenv("SMS_URL"), json=payload)

        print(response.json())

        # if sent the succesfuly, save code in db
        if response.json()["responseCode"] == 200:
            self.otp = OtpCode(
                code=self.otp_code,
                phone_number=self.phone_number,
                generated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            )
            self.save_otp_code()
            return GenerateOtpResponse()
        else:
            return OtpErrorResponse()

    def sms_payload(self):
        return {
            "username": os.getenv("USER_NAME"),
            "password": os.getenv("PASSWORD"),
            "senderId": os.getenv("SENDER_ID"),
            "messageType": int(os.getenv("MESSAGE_TYPE")),
            "msisdn": self.phone_number,
            "message": os.getenv("MESSAGE") + str(self.otp_code),
        }

    def save_otp_code(self):
        db.session.add(self.otp)
        db.session.commit()
