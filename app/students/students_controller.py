from fastapi import APIRouter

from app.pets.pets_service import pets_service
from app.shared import ApiResponse
from app.students.students_schemas import CreateStudentDto, UpdateStudentDto
from app.students.students_service import students_service

router = APIRouter(prefix="/api/students", tags=["Students"])


@router.get("")
def find_all():
    students = students_service.find_all()

    return ApiResponse(
        success=True,
        message="Lista de estudiantes recuperada",
        data=students,
        error=None,
    )


@router.get("/{student_id}")
def find_by_id(student_id: str):
    student = students_service.find_by_id(student_id)

    return ApiResponse(
        success=True,
        message="Estudiante obtenido con éxito",
        data=student,
        error=None,
    )


@router.post("", status_code=201)
def create(body: CreateStudentDto):
    student = students_service.create(body)

    return ApiResponse(
        success=True,
        message="Estudiante creado con éxito",
        data=student,
        error=None,
    )


@router.patch("/{student_id}")
def update(student_id: str, body: UpdateStudentDto):
    student = students_service.update(student_id, body)

    return ApiResponse(
        success=True,
        message="Estudiante actualizado con éxito",
        data=student,
        error=None,
    )


@router.delete("/{student_id}")
def delete(student_id: str):
    deleted = students_service.delete(student_id)
    pets_service.delete_all_for_student(student_id)

    return ApiResponse(
        success=True,
        message="Estudiante eliminado con éxito",
        data=deleted,
        error=None,
    )