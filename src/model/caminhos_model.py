from pydantic import BaseModel
from model.matrix_model import Ponto

class CaminhoCalculado(BaseModel):
    caminho: list[Ponto]
    distancia: float

class MenorCaminhoResponse(BaseModel):
    caminho: list[Ponto]
    distancia: float
