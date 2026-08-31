from typing import List

from model import Rota
from modulefinder import MenorRotaResponse


 
 
class RotaUtils:
    @staticmethod
    def encontrar_menor_rota(rotas: List[Rota]) -> MenorRotaResponse:
        """
        Recebe todas as possibilidades de caminho com suas respectivas
        distâncias, ordena pelo valor da distância e retorna o menor
        caminho junto com sua distância.
        """
        if not rotas:
            raise ValueError("A lista de rotas não pode estar vazia.")
 
        rotas_ordenadas = sorted(rotas, key=lambda rota: rota.distancia)
        menor_rota = rotas_ordenadas[0]
 
        return MenorRotaResponse(
            caminho=menor_rota.caminho,
            distancia=menor_rota.distancia,
        )
