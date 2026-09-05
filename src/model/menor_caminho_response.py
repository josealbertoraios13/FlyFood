from pydantic import BaseModel

from model.ponto import Ponto


class MenorCaminhoResponse(BaseModel):
    caminho: list[Ponto]
    distancia: float