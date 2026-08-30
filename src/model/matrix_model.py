from typing import List, Optional
from pydantic import BaseModel, field_validator

class MatrixInput(BaseModel):
    matrix: List[List[str]]

    @field_validator("matrix")
    @classmethod
    def validate_matrix(cls, value):
        if not value or not value[0]:
            raise ValueError("A matriz não pode estar vazia.")
        largura = len(value[0])
        if any(len(linha) != largura for linha in value):
            raise ValueError("Todas as linhas da matriz devem ter o mesmo tamanho.")
        return value

class Ponto(BaseModel):
    x: int
    y: int 

class MatrixResponse(BaseModel):
    matrix: List[List[Optional[Ponto]]]
    start: Ponto
