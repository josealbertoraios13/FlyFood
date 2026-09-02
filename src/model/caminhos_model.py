from typing import List
from pydantic import BaseModel
from model.matrix_model import Ponto

class CaminhoCalculado(BaseModel):
    caminho: List[Ponto]
    distancia: float

class MenorCaminhoResponse(BaseModel):
    caminho: List[Ponto]
    distancia: float
