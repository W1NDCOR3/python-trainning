from fastapi import FastAPI
from src.routers import router
from src.middleware import LogMiddleware

app = FastAPI(
    title="FastAPI Lab",
    description="A simple API using FastAPI",
    version="0.1.0"
)

app.add_middleware(LogMiddleware)
app.include_router(router)

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}