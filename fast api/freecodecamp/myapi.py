from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel


class Student(BaseModel):
    name: str
    rollNo: int
    branch: str


# data
students = {
    1: {
        "name": "Tarun",
        "rollNo": 1,
        "branch": "CS"
    },
    2: {
        "name": "Nishant",
        "rollNo": 2,
        "branch": "ETC"
    }
}

app = FastAPI()


@app.get('/health')
def health_check() -> str:
    return {"message": "Everything's up!"}


@app.get('/')
def welcome() -> str:
    return "Welcome to my app!"


@app.get('/student/{student_id}')
def student_get(student_id: int = Path(None, description="The ID of the student", gt=0)) -> str:
    return students[student_id] if student_id in students else "Student not found!"


@app.get('/student')
async def student_filter(name: Optional[str] = None) -> str:
    if not name:
        return students
    for _, student in students.items():
        if student['name'].lower() == name.lower():
            return student
    return "Student with name %s not found" % name


@app.post('/student')
def create_student(student: Student):
    # Get the new index first
    new_id = max(students.keys()) + 1
    students[new_id] = student
    return students[new_id]
