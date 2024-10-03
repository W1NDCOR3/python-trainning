from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class User(Base):
    """
    User model class representing a user in the database.

    Since 2.0, SQLAlchemy provides a new way to define mapped attributes using the `mapped_column` function.
    https://docs.sqlalchemy.org/en/20/changelog/whatsnew_20.html#migrating-an-existing-mapping

    Attributes:
        id (int): The unique identifier of the user.
        name (str): The name of the user.

    Methods:
        __repr__(): Returns a string representation of the User object.
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    __table_args__ = {'extend_existing': True}

    def __repr__(self):
        return f"<User(name={self.name})>"
    
class Company(Base):
    """
    Company model class representing a company in the database.

    Since 2.0, SQLAlchemy provides a new way to define mapped attributes using the `mapped_column` function.
    https://docs.sqlalchemy.org/en/20/changelog/whatsnew_20.html#migrating-an-existing-mapping

    Attributes:
        id (int): The unique identifier of the company.
        name (str): The name of the company.

    Methods:
        __repr__(): Returns a string representation of the Company object.
    """

    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    __table_args__ = {'extend_existing': True}

    def __repr__(self):
        return f"<Company(name={self.name})>"
