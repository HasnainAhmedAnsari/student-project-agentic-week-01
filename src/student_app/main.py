import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = PROJECT_ROOT / "src"

if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from dotenv import load_dotenv

load_dotenv(PROJECT_ROOT / ".env")

from student_app.config import APP_NAME, DEBUG, MAX_STUDENTS
from student_app.logger import logger
from student_app.utils.validation import validate_name, validate_marks
from student_app.services.calculator import calculate_grade

STUDENT_FILE = PROJECT_ROOT / "data" / "student.json"


def load_student():
    with open(STUDENT_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    logger.info("Application started")

    try:
        student = load_student()
    except FileNotFoundError:
        logger.error("Student JSON file was not found")
        print("Error: data/student.json is missing.")
        return
    except json.JSONDecodeError:
        logger.error("Student JSON file contains invalid JSON")
        print("Error: student.json contains invalid JSON.")
        return
    except OSError:
        logger.exception("Could not read student data")
        print("Error: Could not read student data.")
        return

    if not isinstance(student, dict):
        logger.error("Student JSON must contain an object")
        print("Error: Invalid student data format.")
        return

    required_fields = ("id", "name", "program", "semester", "marks")
    if any(field not in student for field in required_fields):
        logger.error("Required student fields are missing")
        print("Error: Student information is incomplete.")
        return

    if not validate_name(student["name"]):
        logger.warning("Invalid student name")
        print("Error: Student name cannot be empty.")
        return

    if not validate_marks(student["marks"]):
        logger.warning("Invalid marks: %r", student["marks"])
        print("Error: Marks must be a number between 0 and 100.")
        return

    grade = calculate_grade(student["marks"])

    logger.info("Student information loaded successfully")

    print(f"Starting: {APP_NAME}")
    print(f"Debug Mode: {DEBUG}")
    print(f"Maximum Students: {MAX_STUDENTS}")
    print("\nStudent Information")
    print("-------------------")
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Program: {student['program']}")
    print(f"Semester: {student['semester']}")
    print(f"Marks: {student['marks']}")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()