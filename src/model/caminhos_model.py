from typing import List
from pydantic import BaseModel
from model.matrix_model import Ponto

# --- Models novos para a task "menor caminho" ---

class CaminhoCalculado(BaseModel):
    caminho: List[Ponto]
    distancia: float

class MenorCaminhoResponse(BaseModel):
    caminho: List[Ponto]
    distancia: float
