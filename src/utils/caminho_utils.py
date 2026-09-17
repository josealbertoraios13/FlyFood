from model import Ponto


class CaminhoUtils:

    @staticmethod
    def calcular_caminho(caminho : list[Ponto]) -> int:
        tamanho_do_caminho : int = 0
        for i, ponto in enumerate(caminho):
            if i + 1 >= len(caminho):
                tamanho_do_caminho += abs(ponto.x - caminho[0].x) + abs(ponto.y - caminho[0].y)
                break

            tamanho_do_caminho += abs(ponto.x - caminho[i + 1].x) + abs(ponto.y - caminho[i + 1].y)

        return tamanho_do_caminho