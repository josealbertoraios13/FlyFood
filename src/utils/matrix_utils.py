from itertools import permutations

from model import MatrixResponse, Ponto


class MatrixUtils:
    @staticmethod
    def matriz_para_pontos(matriz: list[list[str]]) -> MatrixResponse:
        start: Ponto | None = None
        matriz_pontos: list[list[Ponto | None]] = []

        for y, linha in enumerate(matriz):
            linha_pontos: list[Ponto | None] = []

            for x, celula in enumerate(linha):
                valor = str(celula).strip().upper()

                if valor == "I":
                    if start is not None:
                        raise ValueError(
                            "A matriz não pode ter mais de um ponto inicial 'I'."
                        )

                    start = Ponto(x=x, y=y)
                    linha_pontos.append(start)

                elif valor == "P":
                    linha_pontos.append(Ponto(x=x, y=y))

                else:
                    linha_pontos.append(None)

            matriz_pontos.append(linha_pontos)

        if start is None:
            raise ValueError(
                "A matriz deve conter exatamente um ponto inicial 'I'."
            )

        return MatrixResponse(
            matrix=matriz_pontos,
            start=start
        )

    @staticmethod
    def gerar_possibilidades(
        matrix_response: MatrixResponse
    ) -> list[list[Ponto]]:
        pontos: list[Ponto] = []

        for linha in matrix_response.matrix:
            for ponto in linha:
                if ponto is not None and ponto != matrix_response.start:
                    pontos.append(ponto)

        possibilidades: list[list[Ponto]] = []

        for permutacao in permutations(pontos):
            caminho = [matrix_response.start, *permutacao]
            possibilidades.append(caminho)

        return possibilidades
