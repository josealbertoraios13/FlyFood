from pydantic import BaseModel

from model.ponto import Ponto


class MatrixResponse(BaseModel):
    matrix: list[list[Ponto | None]]
    start: Ponto