from fastapi import APIRouter
from src.models import Message

router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Hello, World!"}