from itertools import permutations

from model import MatrixResponse, MenorCaminhoResponse, Ponto
from utils.caminho_utils import CaminhoUtils


class MatrixUtils:
    @staticmethod
    def matriz_para_pontos(matriz: list[list[str]]) -> MatrixResponse:
        start: Ponto | None = None
        pontos: dict[str, Ponto] = {}
        matriz_pontos: list[list[Ponto | int]] = []

        for y, linha in enumerate(matriz):
            linha_pontos: list[Ponto | int] = []

            for x, celula in enumerate(linha):
                valor = str(celula).strip().upper()

                if valor == "R":
                    if start is not None:
                        raise ValueError(
                            "A matriz não pode ter mais de um ponto inicial 'R'."
                        )

                    start = Ponto(x=x, y=y)
                    linha_pontos.append(start)

                elif len(valor) == 1 and valor.isalpha():
                    if valor in pontos:
                        raise ValueError(f"A letra '{valor}' aparece mais de uma vez na matriz.")
                    ponto = Ponto(x=x, y=y)
                    pontos[valor] = ponto
                    linha_pontos.append(ponto)

                else:
                    linha_pontos.append(0)

            matriz_pontos.append(linha_pontos)

        if start is None:
            raise ValueError(
                "A matriz deve conter exatamente um ponto inicial 'R'."
            )

        if not pontos:
            raise ValueError("A matriz deve conter ao menos um ponto de entrega.")
        
        return MatrixResponse(
            matrix=matriz_pontos,
            start=start,
            pontos=pontos
        )

    @staticmethod
    def ver_possibilidades(matrix_response: MatrixResponse) -> MenorCaminhoResponse:
        caminho : list[Ponto] = []
        tamanho_do_caminho : int = 0

        for permutacao in permutations(matrix_response.pontos.values()):
            caminho_atual : list[Ponto] = [matrix_response.start, *permutacao]

            tamanho_do_caminho_atual : int = CaminhoUtils.calcular_caminho(caminho=caminho_atual)

            if len(caminho) == 0:
                caminho = caminho_atual
                tamanho_do_caminho = tamanho_do_caminho_atual
                continue

            if tamanho_do_caminho_atual <= tamanho_do_caminho:
                caminho = caminho_atual
                tamanho_do_caminho = tamanho_do_caminho_atual
                continue

        return MenorCaminhoResponse(caminho=caminho, tamanho_do_caminho=tamanho_do_caminho)