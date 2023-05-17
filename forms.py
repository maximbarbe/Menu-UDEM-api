from dataclasses import dataclass
from fastapi import Form



@dataclass
class RegisterForm:
    username: str = Form(...)
    email: str = Form(...)
    password: str = Form(...)
    confirmed_password: str = Form(...)