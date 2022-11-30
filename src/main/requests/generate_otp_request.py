import os

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class GenerateOtpRequest(BaseModel):
    phone_number: str
