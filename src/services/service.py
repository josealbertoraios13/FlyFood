import time

from model import CaminhoCalculado, MatrixResponse, MenorCaminhoResponse, Ponto
from utils import CaminhoUtils, MatrixUtils


def processar_matrix(matrix_str : list[list[str]]) -> MenorCaminhoResponse:
    inicio_time = time.perf_counter()

    matrix_response : MatrixResponse = MatrixUtils.matriz_para_pontos(matrix_str)

    possibilidades_de_caminhos : list[list[Ponto]] = MatrixUtils.gerar_possibilidades(matrix_response=matrix_response)

    caminhos_calculados : list[CaminhoCalculado] = CaminhoUtils.calcular_caminhos(caminhos=possibilidades_de_caminhos)

    meno_rota = CaminhoUtils.encontrar_o_menor(caminhos_calculados=caminhos_calculados)

    fim_time = time.perf_counter()
    meno_rota.tempo_resolucao = round((fim_time - inicio_time) * 1000, 2)

    return meno_rota
