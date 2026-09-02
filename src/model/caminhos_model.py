from typing import List
from pydantic import BaseModel
from model.matrix_model import Ponto

# --- Models novos para a task "menor caminho" ---

class CaminhoCalculado(BaseModel):
    """Representa uma possibilidade de caminho já com a distância calculada."""
    caminho: List[Ponto]
    distancia: float

class MenorCaminhoResponse(BaseModel):
    """Resultado final: o melhor caminho encontrado e sua distância."""
    caminho: List[Ponto]
    distancia: float
