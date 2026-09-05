from model import CaminhoCalculado, MenorCaminhoResponse


@staticmethod
def encontrar_menor_caminho(
    possibilidades: list[CaminhoCalculado],
) -> MenorCaminhoResponse:
   
    if not possibilidades:
        raise ValueError("A lista de possibilidades não pode estar vazia.")

    possibilidades_ordenadas = sorted(
        possibilidades, key=lambda p: p.distancia
    )

    menor = possibilidades_ordenadas[0]

    return MenorCaminhoResponse(
        caminho=menor.caminho,
        distancia=menor.distancia,
    )
