from fastapi import APIRouter

from app.shared import ApiResponse
from app.pets.pets_schemas import CreatePetDto, UpdatePetDto
from app.pets.pets_service import pets_service

router = APIRouter(
    prefix="/api/students/{studentId}/pets",
    tags=["Pets"],
)

@router.get("")
def find_all(studentId: str):
    pets = pets_service.find_all_for_student(studentId)
    return ApiResponse(
        success=True,
        message="Lista de mascotas recuperada",
        data=pets,
        error=None,
    )

@router.post("", status_code=201)
def create(studentId: str, body: CreatePetDto):
    new_pet = pets_service.create(studentId, body)
    return ApiResponse(
        success=True,
        message="Mascota creada con éxito",
        data=new_pet,
        error=None,
    )

@router.patch("/{petId}")
def update(studentId: str, petId: str, body: UpdatePetDto):
    updated_pet = pets_service.update(studentId, petId, body)
    return ApiResponse(
        success=True,
        message="Mascota actualizada con éxito",
        data=updated_pet,
        error=None,
    )

@router.delete("/{petId}")
def delete(studentId: str, petId: str):
    deleted_pet = pets_service.delete(studentId, petId)
    return ApiResponse(
        success=True,
        message="Mascota eliminada con éxito",
        data=deleted_pet,
        error=None,
    )
    