from sqlalchemy.orm import DeclarativeBase, Mapped

class BaseModel(DeclarativeBase)
    pass

class Company(BaseModel):
    
    __tablename__="companies"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]= mapped_column(unique=True)
    