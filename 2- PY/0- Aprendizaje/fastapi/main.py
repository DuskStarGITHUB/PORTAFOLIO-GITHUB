"""Titulo: |FastApi|"""
#####################################################################################
# Descripción: <Fast Api aprendizaje>
# Autor: <DuskStar>
# Fecha de creación: <08/09/2023>
# Nota: <N/A>
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
