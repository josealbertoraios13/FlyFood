
from typing import List, Optional
from model.matrix_model import (
    MatrixInput,
    Ponto,
    MatrixResponse,
    CaminhoAvaliado,
    MenorCaminhoResponse,
)


def matriz_para_pontos(matriz: List[List[str]]) -> MatrixResponse:
    start: Optional[Ponto] = None
    matriz_pontos: List[List[Optional[Ponto]]] = []

    for y, linha in enumerate(matriz):
        linha_pontos: List[Optional[Ponto]] = []
        for x, celula in enumerate(linha):
            valor = str(celula).strip().upper()
            if valor == "I":
                if start is not None:
                    raise ValueError("A matriz não pode ter mais de um ponto inicial 'I'.")
                start = Ponto(x=x, y=y)
                linha_pontos.append(start)
            elif valor == "P":
                linha_pontos.append(Ponto(x=x, y=y))
            else:
                linha_pontos.append(None)
        matriz_pontos.append(linha_pontos)

    if start is None:
        raise ValueError("A matriz deve conter exatamente um ponto inicial 'I'.")

    return MatrixResponse(matrix=matriz_pontos, start=start)


def encontrar_menor_caminho(
    possibilidades: List[CaminhoAvaliado],
) -> MenorCaminhoResponse:
    """
    Recebe todas as possibilidades de caminho junto com suas distâncias,
    ordena pelo valor da distância e retorna o menor caminho encontrado
    junto com sua respectiva distância.
    """
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