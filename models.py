
from fastapi import APIRouter

pages_router = APIRouter(prefix="/pages")


@pages_router.get('/')
async def landing():
    return {
        "message": "This is landing."
    }


@pages_router.get('/shop')
async def shop():
    return {
        "habar": "Shop page"
    }


@pages_router.get('/cart')
async def cart():
    return {
        "habar": "cart page"
    }


@pages_router.get('/detail')
async def detail():
    return {
        "habar": "Detail page"
    }


