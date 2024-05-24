from fastapi import FastAPI
from auth import auth_router
from models import pages_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(pages_router)


@app.get('/')
async def home():
    return {
        "message": "This is home"
    }