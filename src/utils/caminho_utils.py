from model import CaminhoCalculado, MenorCaminhoResponse, Ponto


class CaminhoUtils:
    @staticmethod
    def encontrar_o_menor(caminhos_calculados: list[CaminhoCalculado]) -> MenorCaminhoResponse:
        if not caminhos_calculados:
            raise ValueError("A lista de possibilidades não pode estar vazia.")

        caminhos_calculados_ordenados = sorted(
            caminhos_calculados, key=lambda p: p.tamanho_do_caminho
        )

        menor = caminhos_calculados_ordenados[0]

        print("Menor caminho retornado com sucesso")
        return MenorCaminhoResponse(
            caminho=menor.caminho,
            distancia=menor.tamanho_do_caminho,
        )

    @staticmethod
    def calcular_caminho(caminho : list[Ponto]) -> float:
        tamanho_do_caminho : int = 0
        for i, ponto in enumerate(caminho):
            if i + 1 >= len(caminho):
                tamanho_do_caminho += abs(ponto.x - caminho[0].x) + abs(ponto.y - caminho[0].y)

            tamanho_do_caminho += abs(ponto.x - caminho[i + 1].x) + abs(ponto.y - caminho[i + 1].y)

        return tamanho_do_caminho