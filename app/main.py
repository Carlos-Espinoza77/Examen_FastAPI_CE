#Importa la clase principal que permite la aplicación web de FastAPI
from fastapi import FastAPI

from app.config import settings
from app.database import models
from app.database.database import Base, engine
from app.routes.users import router as user_router
from app.routes.posts import router as post_router


#Se crea la instancia principal de la aplicacion FASTAPI
app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
)

Base.metadata.create_all(bind=engine)
app.include_router(user_router)
app.include_router(post_router)
#Corresponde a la ruta principal de la aplicación
@app.get("/")
def inicio() -> dict[str, str]:  # indica que la función devuelve un diccionario con claves y valores de texto
    return {
        "message": "La aplicación FastAPI funciona correctamente"  # FASTAPI convierte automáticamente este diccionario en JSON
    }
