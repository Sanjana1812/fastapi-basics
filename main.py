```python
# Import FastAPI framework
from fastapi import FastAPI

# Import BaseModel for validation
from pydantic import BaseModel


# Create FastAPI app object
app = FastAPI()


# -----------------------------
# Pydantic Model (Request Body)
# -----------------------------
# Used to validate incoming JSON data

class User(BaseModel):
    name: str
    age: int


# -----------------------------
# Home Route
# -----------------------------
# Simple GET request

@app.get("/")
def home():
    return {
        "message": "API Running"
    }


# -----------------------------
# POST Request
# -----------------------------
# Accept user data from request body

@app.post("/user")
def create_user(user: User):

    return {
        "message": "User created",
        "data": user
    }


# -----------------------------
# Path Parameter Example
# -----------------------------
# user_id comes from URL

@app.get("/user/{user_id}")
def get_user(user_id: int):

    return {
        "user_id": user_id
    }


# -----------------------------
# Query Parameter Example
# -----------------------------
# Values come after ?

@app.get("/search")
def search(name: str, age: int):

    return {
        "name": name,
        "age": age
    }


# -----------------------------
# Path + Query Parameter
# -----------------------------
# product_id → Path
# category → Query

@app.get("/product/{product_id}")
def get_product(product_id: int, category: str):

    return {
        "product_id": product_id,
        "category": category
    }


# -----------------------------
# Multiple Parameters Example
# -----------------------------
# roll_no → Path
# name, age → Query

@app.get("/student/{roll_no}")
def student(
    roll_no: int,
    name: str,
    age: int
):

    return {
        "roll": roll_no,
        "name": name,
        "age": age
    }
```
