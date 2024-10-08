import asyncpg
from src.config import POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST


async def connect():

    return await asyncpg.connect(
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        database=POSTGRES_DB,
        host=POSTGRES_HOST,
    )


async def create_table() -> bool:
    """
    Creates a table named 'items' in the database with the following columns:
        - id: SERIAL PRIMARY KEY
        - name: TEXT NOT NULL
        - description: TEXT NOT NULL

    Returns:
        bool: True if the table is created successfully, False if the table already exists.
    """
    try:
        conn = await connect()

        await conn.execute(
            """
            CREATE TABLE users (
                id SERIAL PRIMARY KEY,
                first_name TEXT NOT NULL,
                second_name TEXT NOT NULL,
                gender TEXT NOT NULL
            )
            """
        )
        await conn.close()

    except asyncpg.exceptions.DuplicateTableError:
        return False
    return True


async def insert_user(first_name: str, second_name: str, gender: str) -> bool:
    try:
        conn = await connect()

        await conn.execute(
            "INSERT INTO users (name, description) VALUES ($1, $2, $3)", first_name, second_name, gender
        )
        await conn.close()

    except asyncpg.exceptions.UndefinedTableError:
        return False
    return True


async def get_male_users() -> list:
    """
    Retrieves a list of items from the database.

    Returns:
        list: A list of items retrieved from the database.

    Raises:
        asyncpg.exceptions.UndefinedTableError: If the 'users' table does not exist in the database.
    """
    try:
        conn = await connect()
        users: list = await conn.fetch("SELECT * FROM users WHERE gender =='M'")

        await conn.close()
        return users

    except asyncpg.exceptions.UndefinedTableError:
        return []
    
async def get_female_users() -> list:
    """
    Retrieves a list of items from the database.

    Returns:
        list: A list of items retrieved from the database.

    Raises:
        asyncpg.exceptions.UndefinedTableError: If the 'items' table does not exist in the database.
    """
    try:
        conn = await connect()
        users: list = await conn.fetch("SELECT * FROM users WHERE gender =='F'")

        await conn.close()
        return users

    except asyncpg.exceptions.UndefinedTableError:
        return []
