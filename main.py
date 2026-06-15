from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.get("/")
def home():
    return {"message": "API Running"}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }
@app.get("/search")
def search(name: str, age: int):
    return {
        "name": name,
        "age": age
    }
@app.get("/product/{product_id}")
def get_product(product_id: int, category: str):
    return {
        "product_id": product_id,
        "category": category
    }
@app.get("/student/{roll_no}")
def student(roll_no:int, name:str, age:int):
    return {
        "roll": roll_no,
        "name": name,
        "age": age
    }
# -----------------------------
# PUT Request (Update Data)
# -----------------------------

@app.put("/user/{user_id}")
def update_user(user_id: int, user: User):

    return {
        "message": "User updated",
        "user_id": user_id,
        "data": user
    }
# -----------------------------
# DELETE Request
# -----------------------------
# Delete user by ID

@app.delete("/user/{user_id}")
def delete_user(user_id: int):

    return {
        "message": "User deleted",
        "user_id": user_id
    }
@app.delete("/product/{product_id}")
def delete_product(product_id:int):

    return{
 "message": "Product deleted",
 "product_id": product_id
}
# -----------------------------
# POST + Query + Body
# -----------------------------

@app.post("/register")
def register_user(
    role: str,
    user: User
):

    return {
        "message": "Registration successful",
        "role": role,
        "user": user
    }
