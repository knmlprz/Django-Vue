from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import (
    csrf_exempt,
    ensure_csrf_cookie,
)
from ninja import NinjaAPI, Swagger

from users.auth import router as auth_router

api = NinjaAPI(
    csrf=True,
    docs=Swagger(
        settings={"persistAuthorization": True},
    ),
    title="Demo API",
    description="This is a demo API with dynamic OpenAPI info section",
)


@api.post("/csrf")
@ensure_csrf_cookie
@csrf_exempt
def get_csrf_token(request: HttpRequest):
    return HttpResponse()


api.add_router("auth/", auth_router)
