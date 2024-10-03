# models/__init__.py
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .user import User
from .user import Company
