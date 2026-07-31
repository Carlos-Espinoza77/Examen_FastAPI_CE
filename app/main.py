#Importa la clase principal que permite la aplicación web de FastAPI
from fastapi import FastAPI

#Se crea la instancia principal de la aplicacion FASTAPI
app = FastAPI(
    title="Examen FastAPI",
    description="API REST de usuarios, publicaciones y comentarios",
    version="1.0.0", #versión inicial del proyecto a implementar
)

#Corresponde a la ruta principal de la aplicación
@app.get("/")
def inicio() -> dict[str, str]: #indica que la función devuelve un diccionario con claves y valores de texto
    return {
        "message": "La aplicación FastAPI funciona correctamente" #FASTAPI convierte automáticamente este diccionario en JSON
    }