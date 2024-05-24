from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth")


@auth_router.get("/")
async def auth():
    return {
        "habar": "auth habarlari bolishi kerak"
    }


@auth_router.get("/login")
async def login():
    return {
        "habar": "login habarlari bolishi kerak"
    }


@auth_router.get("/register")
async def register():
    return {
        "habar": "register bo'limi"
    }


@auth_router.get("/log-out")
async def logout():
    return {
        "habar": "logout"
    }

