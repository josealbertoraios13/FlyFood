from typing import List, Optional
from model.matrix_model import (
    MatrixInput,
    Ponto,
    MatrixResponse,
)

from model.caminhos_model import CaminhoAvaliado, MenorCaminhoResponse

def encontrar_menor_caminho(
    possibilidades: List[CaminhoAvaliado],
) -> MenorCaminhoResponse:
   
    if not possibilidades:
        raise ValueError("A lista de possibilidades não pode estar vazia.")

    # 1. Ordenar pelo valor da distância
    possibilidades_ordenadas = sorted(
        possibilidades, key=lambda p: p.distancia
    )

    # 2. Pegar a menor
    menor = possibilidades_ordenadas[0]

    # 3. Retornar: menor caminho + sua respectiva distância
    return MenorCaminhoResponse(
        caminho=menor.caminho,
        distancia=menor.distancia,
    )