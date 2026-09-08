from pydantic import BaseModel

from model.ponto import Ponto


class MenorCaminhoResponse(BaseModel):
    caminho: list[Ponto]
    distancia: float
    tempo_resolucao_ms: float = 0.0