from typing import List, Optional
from model.matrix_model import MatrixInput, Ponto, MatrixResponse, Caminho
 
def matriz_para_pontos(matriz: List[List[str]]) -> MatrixResponse:
    start: Optional[Ponto] = None
    matriz_pontos: List[List[Optional[Ponto]]] = []
 
    for y, linha in enumerate(matriz):
        linha_pontos: List[Optional[Ponto]] = []
        for x, celula in enumerate(linha):
            valor = str(celula).strip().upper()
            if valor == "I":
                if start is not None:
                    raise ValueError("A matriz não pode ter mais de um ponto inicial 'I'.")
                start = Ponto(x=x, y=y)
                linha_pontos.append(start)
            elif valor == "P":
                linha_pontos.append(Ponto(x=x, y=y))
            else:
                linha_pontos.append(None)
        matriz_pontos.append(linha_pontos)
 
    if start is None:
        raise ValueError("A matriz deve conter exatamente um ponto inicial 'I'.")
 
    return MatrixResponse(matrix=matriz_pontos, start=start)
 
 
def encontrar_menor_caminho(possibilidades: List[Caminho]) -> Caminho:
    """
    Recebe todas as possibilidades de caminho já com a distância de cada uma
    calculada, ordena pelo valor da distância e retorna a possibilidade com
    a menor distância (o menor caminho + sua respectiva distância).
 
    Exemplo (baseado no enunciado da task):
        S -> A -> B -> C -> D = 25
        S -> A -> C -> B -> D = 18
        S -> B -> D -> A -> C = 31
        S -> D -> C -> B -> A = 12  <- MENOR
        S -> C -> A -> D -> B = 27
 
        encontrar_menor_caminho(possibilidades) retorna o caminho
        "S -> D -> C -> B -> A" com distancia = 12.
    """
    if not possibilidades:
        raise ValueError("A lista de possibilidades não pode estar vazia.")
 
    possibilidades_ordenadas = sorted(
        possibilidades, key=lambda caminho: caminho.distancia
    )
 
    return possibilidades_ordenadas[0]
