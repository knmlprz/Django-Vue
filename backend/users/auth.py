from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from ninja import Router
from ninja.errors import HttpError
from ninja.security import django_auth

from .models import CustomUser
from .schemas import (
    LoginSchema,
    RegisterSchema,
    UserSchema,
)

router = Router(tags=["Authentication"])


@router.post("/login", response={200: UserSchema})
@csrf_exempt
def login_user(request: HttpRequest, credentials: LoginSchema):
    user = authenticate(username=credentials.email, password=credentials.password)

    if user is None:
        raise HttpError(400, "Incorrect email or password")

    login(request, user)
    return user


@router.post("/register", response={200: UserSchema})
@csrf_exempt
def register_user(request: HttpRequest, credentials: RegisterSchema):
    # Validate password
    if credentials.password != credentials.password_confirm:
        raise HttpError(400, "Passwords do not match")

    # Check if user exists
    if CustomUser.objects.filter(email=credentials.email).exists():
        raise HttpError(400, "Email is already in use. Please login.")

    # Create user
    user = CustomUser.objects.create(
        email=credentials.email,
    )

    user.set_password(credentials.password)
    user.save()

    return user


@router.post("/logout", auth=django_auth)
def logout_user(request: HttpRequest):
    logout(request)
    return {"detail": "Successfully logged out"}


@router.get("/user", auth=django_auth, response={200: UserSchema})
def get_user(request: HttpRequest):
    return request.user
