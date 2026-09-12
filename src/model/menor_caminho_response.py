from pydantic import BaseModel

from model.ponto import Ponto


class MenorCaminhoResponse(BaseModel):
    caminho: list[Ponto]
    distancia: float
    tempo_resolucao: float = 0.0
    caminho_formatado: str = ""

    @staticmethod
    def formatar_resultado(caminho: list[Ponto], distancia: int) -> str:
        if not caminho:
            return ""

        caminho_str = "->".join(f"({ponto.x},{ponto.y})" for ponto in caminho)
        return f"{caminho_str} | Distância: {distancia}"