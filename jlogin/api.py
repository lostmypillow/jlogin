from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, Schema
from student.models import *

api = NinjaAPI()


class StudentIn(Schema):
    student_id: str
    password: int


class StudentOut(Schema):
    student_id: str
    password: int


@api.post("/register")
def create_student(request, payload: StudentIn):
    student = Student.objects.create(**payload.dict())
    return f"Student {payload.student_id} created"


@api.post("/login")
def check_student(request, payload: StudentOut):
    student = get_object_or_404(Student, student_id=payload.student_id, password=payload.password)
    return student

