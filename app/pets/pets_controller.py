from fastapi import APIRouter

from app.pets.pets_schemas import CreatePetDto, Pet, UpdatePetDto
from app.pets.pets_service import pets_service

router = APIRouter(
    prefix="/api/students/{studentId}/pets",
    tags=["Pets"],
)

@router.get("")
def find_all(studentId: str):
    pets = pets_service.find_all_for_student(studentId)
    return {
        "message": "Lista de mascotas recuperada",
        "data": pets
    }

@router.post("", status_code=201)
def create(studentId: str, body: CreatePetDto):
    new_pet = pets_service.create(studentId, body)
    return {
        "message": "Mascota creada con éxito",
        "data": new_pet
    }

@router.patch("/{petId}")
def update(studentId: str, petId: str, body: UpdatePetDto):
    updated_pet = pets_service.update(studentId, petId, body)
    return {
        "message": "Mascota actualizada con éxito",
        "data": updated_pet
    }

@router.delete("/{petId}")
def delete(studentId: str, petId: str):
    deleted_pet = pets_service.delete(studentId, petId)
    return {
        "message": "Mascota eliminada con éxito",
        "data": deleted_pet
    }