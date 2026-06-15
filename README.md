# FastAPI Basics 🚀

This repository contains my beginner practice project built while learning **FastAPI**, **Postman**, and **Swagger UI**.

The goal of this project is to understand how APIs work and how to test them using real backend development tools.

---

## What I Learned

### API Requests

* GET → Retrieve data
* POST → Send/Create data

### FastAPI Concepts

* Creating API endpoints
* Request body using Pydantic
* Data validation
* Status codes

### Parameters

* Path Parameters
* Query Parameters

### API Testing

* Testing APIs using Postman
* Testing APIs using Swagger UI (`/docs`)

---

## Features Implemented

✅ Home API
✅ Create User API
✅ Path Parameter Example
✅ Query Parameter Example
✅ Validation using FastAPI
✅ Swagger Documentation

---

## Project Structure

```plaintext
fastapi-basics/
│
├── main.py
├── README.md
├── requirements.txt
```

---

## Run the Project

Install dependencies:

```bash
pip install fastapi uvicorn
```

Start server:

```bash
uvicorn main:app --reload
```

Server:

```plaintext
http://127.0.0.1:8000
```

Open Swagger Documentation:

```plaintext
http://127.0.0.1:8000/docs
```

---

## Example API

Request:

```http
GET /product/101?category=laptop
```

Response:

```json
{
  "product_id": 101,
  "category": "laptop"
}
```

---

## Learning Outcome

This project helped me understand:

* API development using FastAPI
* API testing workflow
* Difference between Path and Query Parameters
* Validation and debugging
