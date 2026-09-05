from model import CaminhoCalculado, MenorCaminhoResponse, Ponto


class CaminhoUtils:
    @staticmethod
    def encontrar_o_menor(caminhos_calculados: list[CaminhoCalculado]) -> MenorCaminhoResponse:
        print("Rivan")
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
    def calcular_caminhos(caminhos : list[list[Ponto]]) -> list[CaminhoCalculado]:
        caminhos_calculados : list[CaminhoCalculado] = []
        print("Jose")
        for _, caminho in enumerate(caminhos):
            tamanho_do_caminho : int = 0
            for i, ponto in enumerate(caminho):
                if i + 1 >= len(caminho):
                    break

                tamanho_do_caminho += abs(ponto.x - caminho[i + 1].x) + abs(ponto.y - caminho[i + 1].y)

            caminhos_calculados.append(CaminhoCalculado(caminho=caminho, tamanho_do_caminho=tamanho_do_caminho))

        print("todos os caminhos calculados com sucesso")
        return caminhos_calculados