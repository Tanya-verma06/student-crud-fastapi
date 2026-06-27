from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()

students = []

class Student(BaseModel):
    id: int
    name: str
    age: int

# UI
@app.get("/")
def home():
    return FileResponse("static/index.html")

# CREATE
@app.post("/students")
def create(student: Student):
    students.append(student)
    return {"message": "Student Added", "data": student}

# READ
@app.get("/students")
def read():
    return students

# UPDATE
@app.put("/students/{student_id}")
def update(student_id: int, student: Student):
    for i in range(len(students)):
        if students[i].id == student_id:
            students[i] = student
            return {"message": "Updated", "data": student}
    return {"message": "Student Not Found"}

# DELETE
@app.delete("/students/{student_id}")
def delete(student_id: int):
    for i in range(len(students)):
        if students[i].id == student_id:
            students.pop(i)
            return {"message": "Deleted"}
    return {"message": "Student Not Found"}