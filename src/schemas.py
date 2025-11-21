from pydantic import BaseModel
from typing import Optional

class PetBase(BaseModel):
    name: str
    color: Optional[str] = None
    birth_year: Optional[int] = None
    species: Optional[str] = None
    breed: Optional[str] = None

class PetCreate(PetBase):
    pass

class Pet(PetBase):
    id: int

    class Config:
        from_attributes = True
