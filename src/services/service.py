import time

from model import MatrixResponse, MenorCaminhoResponse
from utils import MatrixUtils


def processar_matrix(matrix_str : list[list[str]]) -> MenorCaminhoResponse:
    inicio_time = time.perf_counter()

    matrix_response : MatrixResponse = MatrixUtils.matriz_para_pontos(matrix_str)

    menor_caminho : MenorCaminhoResponse = MatrixUtils.ver_possibilidades(matrix_response=matrix_response)

    letra_por_coordenada = {
        (ponto.x, ponto.y): letra for letra, ponto in matrix_response.pontos.items()
    }

    menor_caminho.rota = " ".join(
        letra_por_coordenada[(ponto.x, ponto.y)]
        for ponto in menor_caminho.caminho
        if (ponto.x, ponto.y) in letra_por_coordenada
    )[::-1]

    fim_time = time.perf_counter()
    menor_caminho.tempo_resolucao = round((fim_time - inicio_time), 2)

    return menor_caminho
