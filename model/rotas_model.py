from typing import List
from pydantic import BaseModel, field_validator
 
from model.matrix_model import Ponto
 
 
class Rota(BaseModel):
    caminho: List[Ponto]
    distancia: float
 
 
class RotasInput(BaseModel):
    rotas: List[Rota]
 
    @field_validator("rotas")
    @classmethod
    def validate_rotas(cls, value):
        if not value:
            raise ValueError("A lista de rotas não pode estar vazia.")
        return value
 
 
class MenorRotaResponse(BaseModel):
    caminho: List[Ponto]
    distancia: float
