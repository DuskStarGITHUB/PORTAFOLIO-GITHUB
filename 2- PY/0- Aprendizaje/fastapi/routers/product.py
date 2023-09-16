"""Titulo: |Router Products|"""
#####################################################################################
# Descripción: <Router>
# Autor: <DuskStar>
# Fecha de creación: <08/09/2023>
# Nota: <N/A>
#####################################################################################

# Libreria
from fastapi import APIRouter, Path, Query
from models.product import Product

# Definicion de router
router = APIRouter()

# Lista
products = [
    {"id": 1,
     "name": "Laptop2",
     "price": 1000},
    {"id": 2,
     "name": "Laptop2",
     "price": 2000}]

# Ruta de productos
@router.get("/products")

def get_products():
    """Función que devuelve una lista"""
    return products

# Ruta especifica
@router.get("/products/{id}")

def get_product(id: int = Path(gt=0)):
    """Función que devuelve un producto"""
    return list(filter(lambda item: item["id"] == id, products))

# Ruta por por informacion especifica

@router.get("/products/")

def get_products_by_price(price: int = Query(gt=0)):
    """Funcion que devuelve producto por informacion especifica"""
    return list(filter(lambda item: item["price"] == price, products))

# Ruta para crear un producto
@router.post("/products")

def create_product(product: Product):
    """Crear un producto en la lista"""
    products.append(product)
    return products

# Ruta para modificar un producto
@router.put("/products/{id}")

def updatelete_product(id: int, product: Product):
    """Funcion que modifica un producto"""
    for i, item in enumerate(products):
        if item["id"] == id:
            products[i]["name"] = product.name
            products[i]["price"] = product.price
    return products

# Ruta par eliminar un producto

@router.delete("/products/{id}")

def delete_product(id:int):
    """Eliminar un producto"""
    for item in products:
        if item["id"] == id:
            products.remove(item)
    return products
