from pydantic import BaseModel

from model.ponto import Ponto


class MatrixResponse(BaseModel):
    matrix: list[list[Ponto | int]]
    start: Ponto
    pontos: dict[str, Ponto]