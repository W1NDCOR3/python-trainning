from fastapi import FastAPI
from pydantic import BaseModel
from src.db import create_table, insert_user, get_male_users, get_female_users

app = FastAPI()

# Define a Pydantic model for the user payload
class UserPayload(BaseModel):
    first_name: str
    second_name: str
    gender: str

@app.get("/maleusers")
async def read_m():
    m_users = await get_male_users()
    return m_users

@app.get("/femaleusers")
async def read_f():
    f_users = await get_female_users()
    return f_users

@app.post("/create")
async def create():
    """
    Asynchronously creates a table and returns the result.
    Returns:
        dict: A dictionary containing the result of creating the table.
    """
    result = await create_table()
    return {"result": result}

# Modify the write method to accept payloads
@app.post("/write")
async def write(user: UserPayload):
    """
    Asynchronously writes a user's data from the provided payload.

    Args:
        user (UserPayload): A Pydantic model containing the user details.

    Returns:
        dict: A dictionary containing the result of the write operation.
    """
    result = await insert_user(user.first_name, user.second_name, user.gender)
    return {"result": result}
