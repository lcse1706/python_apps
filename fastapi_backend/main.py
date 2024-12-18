from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from pydantic import BaseModel

# Konfiguracja FastAPI
app = FastAPI()

# Konfiguracja bazy danych PostgreSQL
DATABASE_URL = "postgresql://postgres:postgres@localhost/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Deklaracja bazowa dla SQLAlchemy
Base = declarative_base()

# Model użytkownika
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

# Tworzenie tabeli w bazie danych
Base.metadata.create_all(bind=engine)

# Schemat danych użytkownika
class UserSchema(BaseModel):
    name: str
    email: str

# Funkcja do tworzenia sesji bazy danych
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint: Dodanie użytkownika
@app.post("/users/")
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Endpoint: Pobranie wszystkich użytkowników
@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

# Endpoint: Usunięcie użytkownika
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}
