from sqlalchemy import Column, Integer, String
from .database import Base

class PetModel(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    color = Column(String)
    birth_year = Column(Integer)
    species = Column(String)
    breed = Column(String)
