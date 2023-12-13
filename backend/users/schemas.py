from ninja import ModelSchema, Schema
from pydantic import EmailStr

from .models import CustomUser


class LoginSchema(Schema):
    email: EmailStr
    password: str


class RegisterSchema(Schema):
    email: EmailStr
    password: str
    password_confirm: str


class UserSchema(ModelSchema):
    class Meta:
        model = CustomUser
        fields = ["email", "date_joined"]
