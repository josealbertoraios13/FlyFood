from typing import List
from pydantic import BaseModel
 
from model.matrix_model import Ponto
 
 
class Rota(BaseModel):
    caminho: List[Ponto]
    distancia: float
