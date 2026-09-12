from pydantic import BaseModel

from model.ponto import Ponto


class MenorCaminhoResponse(BaseModel):
    caminho: list[Ponto]
    rota: str = ""
    distancia: float
    tempo_resolucao: float = 0.0