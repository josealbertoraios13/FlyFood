from model import CaminhoCalculado, MenorCaminhoResponse


class MenorCaminho:
    @staticmethod
    def encontrar(
        caminhos_calculados: list[CaminhoCalculado],
    ) -> MenorCaminhoResponse:
    
        if not caminhos_calculados:
            raise ValueError("A lista de possibilidades não pode estar vazia.")

        caminhos_calculados_ordenados = sorted(
            caminhos_calculados, key=lambda p: p.distancia
        )

        menor = caminhos_calculados_ordenados[0]

        return MenorCaminhoResponse(
            caminho=menor.caminho,
            distancia=menor.distancia,
        )