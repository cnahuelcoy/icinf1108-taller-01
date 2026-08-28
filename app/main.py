# 1. IMPORTACIONES (Arriba del todo, línea 1)
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

from app.pets.pets_controller import router as pets_router
from app.students.students_controller import router as students_router



def get_timestamp() -> str:
    return datetime.now().isoformat(timespec="seconds")



def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI CRUD Students & Pets",
        description="API de un CRUD en memoria para la entidad Student y sus mascotas (Pet)",
        version="1.0",
    )

    # Errores HTTP
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "message": "Operación fallida",
                "data": None,
                "error": exc.detail,
                "timestamp": get_timestamp(),
            },
        )

    #Errores de datos no válidos
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=422,
            content={
                "success": False,
                "message": "Error de validación en los datos enviados",
                "data": None,
                "error": str(exc.errors()),
                "timestamp": get_timestamp(),
            },
        )

    # Errores no controlados del servidor
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": "Ocurrió un error interno en el servidor",
                "data": None,
                "error": "Error interno del servidor.",
                "timestamp": get_timestamp(),
            },
        )

    # Configuración de rutas existentes
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(students_router)
    app.include_router(pets_router)

    return app


app = create_app()