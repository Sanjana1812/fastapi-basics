
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr


# ----------------------------------
# Create FastAPI App
# ----------------------------------

app = FastAPI()


# ----------------------------------
# Student Model
# ----------------------------------

class Student(BaseModel):

    name: str

    email: EmailStr

    age: int = Field(
        gt=0,
        lt=100
    )

    course: str

    active: bool = True


# ----------------------------------
# Temporary Storage
# ----------------------------------

students = []

student_id = 1


# ----------------------------------
# Home
# ----------------------------------

@app.get("/")
def home():

    return {
        "message":
        "Student Management API Running"
    }


# ----------------------------------
# Create Student
# ----------------------------------

@app.post("/student")
def create_student(
    student: Student
):

    global student_id

    data = student.dict()

    data["id"] = student_id

    students.append(data)

    student_id += 1

    return {

        "message":
        "Student created",

        "student":
        data
    }


# ----------------------------------
# Get All Students
# ----------------------------------

@app.get("/student")
def get_students():

    return students


# ----------------------------------
# Get Student By ID
# ----------------------------------

@app.get("/student/{student_id}")
def get_student(
    student_id: int
):

    for student in students:

        if (
            student["id"]
            ==
            student_id
        ):

            return student

    return {

        "message":
        "Student not found"
    }


# ----------------------------------
# Update Student
# ----------------------------------

@app.put("/student/{student_id}")
def update_student(
    student_id: int,
    updated: Student
):

    for student in students:

        if (
            student["id"]
            ==
            student_id
        ):

            student["name"] = updated.name

            student["email"] = updated.email

            student["age"] = updated.age

            student["course"] = updated.course

            student["active"] = updated.active

            return {

                "message":
                "Student updated",

                "student":
                student
            }

    return {

        "message":
        "Student not found"
    }


# ----------------------------------
# Delete Student
# ----------------------------------

@app.delete("/student/{student_id}")
def delete_student(
    student_id: int
):

    for student in students:

        if (
            student["id"]
            ==
            student_id
        ):

            students.remove(student)

            return {

                "message":
                "Student deleted"
            }

    return {

        "message":
        "Student not found"
    }


# ----------------------------------
# Search By Course
# ----------------------------------

@app.get("/search")
def search_student(
    course: str
):

    result = []

    for student in students:

        if (

            student["course"]
            .lower()

            ==

            course.lower()

        ):

            result.append(student)

    return result


# ----------------------------------
# Count Students
# ----------------------------------

@app.get("/count")
def count_students():

    return {

        "total_students":
        len(students)
    }


# ----------------------------------
# Dashboard
# ----------------------------------

@app.get("/dashboard")
def dashboard():

    active = 0

    courses = set()

    for student in students:

        courses.add(
            student["course"]
        )

        if (
            student["active"]
        ):

            active += 1

    return {

        "total_students":
        len(students),

        "active_students":
        active,

        "inactive_students":
        len(students)
        - active,

        "courses":
        len(courses)
    }


# ----------------------------------
# Filter Active
# ----------------------------------

@app.get("/filter")
def filter_students(
    active: bool
):

    result = []

    for student in students:

        if (

            student["active"]

            ==

            active

        ):

            result.append(student)

    return result


# ----------------------------------
# Course Statistics
# ----------------------------------

@app.get("/stats/course")
def course_stats():

    stats = {}

    for student in students:

        course = student["course"]

        if (

            course
            not in stats

        ):

            stats[course] = 0

        stats[course] += 1

    return stats


# ----------------------------------
# Toggle Status
# ----------------------------------

@app.patch(
    "/student/{student_id}/status"
)
def toggle_status(
    student_id: int
):

    for student in students:

        if (

            student["id"]

            ==

            student_id

        ):

            student["active"] = (

                not
                student["active"]

            )

            return student

    return {

        "message":
        "Student not found"
    }


# ----------------------------------
# Sort Students
# ----------------------------------

@app.get("/sort")
def sort_students():

    return sorted(

        students,

        key=lambda x:

        x["age"]

    )


# ----------------------------------
# Delete All
# ----------------------------------

@app.delete("/student")
def clear_students():

    students.clear()

    return {

        "message":
        "All students removed"
    }

