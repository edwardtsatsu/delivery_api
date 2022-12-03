import os
from datetime import datetime
from random import randint

import requests
from dotenv import load_dotenv

from src.main.requests.generate_otp_request import GenerateOtpRequest

load_dotenv()

from src.extensions import db
from src.main.responses.generate_otp_response import (
    GenerateOtpResponse,
    OtpErrorResponse,
)

from ..models.otp_code_model import OtpCode


class GenerateOtpService:
    def __init__(self, body: GenerateOtpRequest):
        self.phone_number = body.phone_number

    def send_otp(self):
        self.otp_code = self._generate_otp()

        response = self._send_sms()

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

    def _sms_payload(self):
        return {
            "username": os.getenv("USER_NAME"),
            "password": os.getenv("PASSWORD"),
            "senderId": os.getenv("SENDER_ID"),
            "messageType": int(os.getenv("MESSAGE_TYPE")),
            "msisdn": self.phone_number,
            "message": os.getenv("MESSAGE") + str(self.otp_code),
        }

    def _send_sms(self):
        return requests.post(url=os.getenv("SMS_URL"), json=self._sms_payload())

    def _generate_otp(self):
        return randint(1000, 9999)

    def save_otp_code(self):
        db.session.add(self.otp)
        db.session.commit()
