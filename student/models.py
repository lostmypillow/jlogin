from django.db import models


class Student(models.Model):
    student_id = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
