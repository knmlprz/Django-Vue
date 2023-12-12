from ninja import Router
from ninja.security import django_auth

router = Router()

@router.get("/login")
def hello(request):
    return "hello world"
