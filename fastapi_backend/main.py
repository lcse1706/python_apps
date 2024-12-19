from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from pydantic import BaseModel

# FastAPI Configuration
app = FastAPI()

# PostgreSQL configuration db       
DATABASE_URL = "postgresql://postgres:postgres@localhost:2022/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Base declaration for SQLAlchemy
Base = declarative_base()

# User Model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

# Creating tables in db
Base.metadata.create_all(bind=engine)

# User Data Schema
class UserSchema(BaseModel):
    name: str
    email: str

# Function to create db session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint: Add User
@app.post("/users/")
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Endpoint: Get all users
@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

# Endpoint: Delete User
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}
