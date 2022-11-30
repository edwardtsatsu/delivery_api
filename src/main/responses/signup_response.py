from pydantic import BaseModel


class AcoountNotCreatedResponse(BaseModel):
    resp_code: str = "022"
    resp_desc: str = "Account could not be created with these details!"


class UserExistResponse(BaseModel):
    resp_code: str = "001"
    resp_desc: str = "User already exists login!"


class AccountCreatedResponse(BaseModel):
    resp_code: str = "000"
    resp_desc: str = "Account created successfully!"
