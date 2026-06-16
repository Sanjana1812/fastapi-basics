# 🎓 Student Management API

A mini backend project built using **FastAPI** to practice API development, CRUD operations, validation, filtering, and API testing.

This project started as FastAPI practice and evolved into a Student Management System with multiple API features.

---

## Project Goal

Build and test REST APIs while learning:

* FastAPI
* CRUD Operations
* Request Body
* Path Parameters
* Query Parameters
* Validation
* API Testing
* Backend Project Structure

---

## Features

### Student Operations

✅ Create Student
✅ Get All Students
✅ Get Student By ID
✅ Update Student
✅ Delete Student
✅ Delete All Students

### Advanced Features

✅ Auto Student ID
✅ Email Validation
✅ Search Students By Course
✅ Filter Students By Active Status
✅ Sort Students By Age
✅ Course Statistics
✅ Dashboard Summary
✅ Toggle Student Status

---

## Technologies Used

* FastAPI
* Pydantic
* Uvicorn
* Postman
* Swagger UI

---

## API Endpoints

| Method | Endpoint                     | Description            |
| ------ | ---------------------------- | ---------------------- |
| POST   | /student                     | Create student         |
| GET    | /student                     | Get all students       |
| GET    | /student/{student_id}        | Get student by ID      |
| PUT    | /student/{student_id}        | Update student         |
| DELETE | /student/{student_id}        | Delete student         |
| DELETE | /student                     | Delete all students    |
| GET    | /search                      | Search by course       |
| GET    | /count                       | Count students         |
| GET    | /dashboard                   | Student summary        |
| GET    | /filter                      | Filter active students |
| GET    | /stats/course                | Course statistics      |
| PATCH  | /student/{student_id}/status | Toggle status          |
| GET    | /sort                        | Sort students          |

---

## Project Structure

```plaintext
student-management-api/
│
├── main.py
├── requirements.txt
├── README.md
```

---

## Run Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run server:

```bash
uvicorn main:app --reload
```

Server:

```plaintext
http://127.0.0.1:8000
```

Open Swagger:

```plaintext
http://127.0.0.1:8000/docs
```

---

## Example Request

POST /student

```json
{
    "name": "Sanjana",
    "email": "abc@gmail.com",
    "age": 22,
    "course": "CSE",
    "active": true
}
```

Example Response:

```json
{
    "message": "Student created",
    "student": {
        "id": 1,
        "name": "Sanjana",
        "email": "abc@gmail.com",
        "age": 22,
        "course": "CSE",
        "active": true
    }
}
```

---

## API Testing

Tested using:

* Postman
* Swagger UI (`/docs`)

---

## Learning Outcome

This project helped me understand:

* REST API Design
* CRUD Operations
* Validation
* Path Parameters
* Query Parameters
* Request Body
* Filtering and Search
* Backend Workflow
* API Testing and Debugging
