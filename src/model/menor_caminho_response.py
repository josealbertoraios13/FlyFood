from pydantic import BaseModel

from model import Ponto


class MenorCaminhoResponse(BaseModel):
    caminho: list[Ponto]
    distancia: float