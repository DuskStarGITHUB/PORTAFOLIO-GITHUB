"""Titulo: |FastApi|"""
#####################################################################################
# Descripción: <Fast Api aprendizaje>
# Autor: <DuskStar>
# Fecha de creación: <08/09/2023>
# Nota: <Tener instalado la libreria de FastApi>
# Nota: <Navegar hasta la carpeta de este archivo y ejecutar uvicorn main:app>
#####################################################################################

# LIBRERIAS
from fastapi import FastAPI
from routers.product import router as product_router

app = FastAPI()

# Ruta directorio base
@app.get("/")

def message():
    """Función que devuelve un mensaje de bienvenida"""
    return {"Nyasu!"}

# Inicializar router
app.include_router(product_router)
