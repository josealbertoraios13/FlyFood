from pydantic import BaseModel

from model.ponto import Ponto


class CaminhoCalculado(BaseModel):
    caminho: list[Ponto]
    tamanho_do_caminho: float