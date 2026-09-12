from itertools import permutations

from model import MatrixResponse, Ponto

class MatrixUtils:
    @staticmethod
    def matriz_para_pontos(matriz: list[list[str]]) -> MatrixResponse:
        start: Ponto | None = None
        pontos: dict[str, Ponto] = {}
        matriz_pontos: list[list[Ponto | int]] = []

        for y, linha in enumerate(matriz):
            linha_pontos: list[Ponto | None] = []

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
    def gerar_possibilidades(matrix_response: MatrixResponse) -> list[list[Ponto]]:
        pontos: list[Ponto] = []
        print("Kauan")
        for linha in matrix_response.matrix:
            for ponto in linha:
                if ponto is not None and ponto != matrix_response.start:
                    pontos.append(ponto)

        possibilidades: list[list[Ponto]] = []

        for permutacao in permutations(matrix_response.pontos):
            caminho = [matrix_response.start, *permutacao]
            possibilidades.append(caminho)

        print("Todas as possibilidades geradas com sucesso")
        return possibilidades
