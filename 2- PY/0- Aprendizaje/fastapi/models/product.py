"""Titulo: |Model Products|"""
#####################################################################################
# Descripción: <Mi primer modelo>
# Autor: <DuskStar>
# Fecha de creación: <08/09/2023>
# Nota: <N/A>
#####################################################################################

from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    """Modelo de un producto"""
    id: Optional[int] = None
    name: str = Field(default="New Product", min_length=5, max_length=20)
    price: float = Field(default=0.0, ge=0, le=10000)
