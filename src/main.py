from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas
from .database import SessionLocal, engine

# Create tables (idempotent)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Pets API", description="CRUD API for Pets using SQLAlchemy and SQLite")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

# --- CRUD Endpoints ---

# Create
@app.post("/pets/", response_model=schemas.Pet)
def create_pet(pet: schemas.PetCreate, db: Session = Depends(get_db)):
    db_pet = models.PetModel(**pet.dict())
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet

# Read All
@app.get("/pets/", response_model=List[schemas.Pet])
def read_pets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pets = db.query(models.PetModel).offset(skip).limit(limit).all()
    return pets

# Read One
@app.get("/pets/{pet_id}", response_model=schemas.Pet)
def read_pet(pet_id: int, db: Session = Depends(get_db)):
    db_pet = db.query(models.PetModel).filter(models.PetModel.id == pet_id).first()
    if db_pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return db_pet

# Update
@app.put("/pets/{pet_id}", response_model=schemas.Pet)
def update_pet(pet_id: int, pet: schemas.PetCreate, db: Session = Depends(get_db)):
    db_pet = db.query(models.PetModel).filter(models.PetModel.id == pet_id).first()
    if db_pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    
    for key, value in pet.dict().items():
        setattr(db_pet, key, value)
    
    db.commit()
    db.refresh(db_pet)
    return db_pet

# Delete
@app.delete("/pets/{pet_id}")
def delete_pet(pet_id: int, db: Session = Depends(get_db)):
    db_pet = db.query(models.PetModel).filter(models.PetModel.id == pet_id).first()
    if db_pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    
    db.delete(db_pet)
    db.commit()
    return {"message": "Pet deleted successfully"}



