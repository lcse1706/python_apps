from fastapi import FastAPI

app = FastAPI()

# Endpoint root
@app.get("/")
def read_root():
    return {"message": "Hello, DevOps Engineer!"}

# Endpoint z parametrem
@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id, "message": "This is your user data"}
