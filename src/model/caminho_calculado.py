from pydantic import BaseModel

from model import Ponto


class CaminhoCalculado(BaseModel):
    caminho: list[Ponto]
    distancia: float