import requests
import random
import concurrent.futures
from time import time

BASE_URL = "http://127.0.0.1:8000/api"
NUM_CLIENTS = 14000

students = []
print("Program start")
total_start_time = time()


def generate_random_string(length=10):
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=length))


def generate_random_integer(length=6):
    return ''.join(random.choices('0123456789', k=length))


def register_student(index):
    student_id = generate_random_string()
    password = generate_random_integer()
    data = {'student_id': student_id, 'password': password}
    start_time = time()
    try:
        response = requests.post(f"{BASE_URL}/register", json=data)
        end_time = time()
        elapsed_time = end_time - start_time
        if response.status_code == 200:
            result = response.json()
            print(
                f"Student {index}: {student_id} registered, password is {password} elapsed: {elapsed_time:.2f} seconds")
            students.append(data)
        else:
            print(
                f"Student {index}: Failed to register student {student_id}, Status Code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Student {index}: Exception occurred: {e}")


def login_student(student):
    start_time = time()
    try:
        response = requests.post(f"{BASE_URL}/login", json=student)
        end_time = time()
        elapsed_time = end_time - start_time
        if response.status_code == 200:
            result = response.json()
            print(f"Student {student['student_id']} logged in,  elapsed: {elapsed_time:.2f} seconds")
        else:
            print(
                f"Failed to login student {student['student_id']}, Status Code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Exception occurred while logging in student {student['student_id']}: {e}")


print("Registering students...")
with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
    executor.map(register_student, range(NUM_CLIENTS))

print("Logging in students...")
with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
    executor.map(login_student, students)
total_end_time = time()
print(f"Program ended in {(total_end_time - total_start_time):.3f} seconds")
