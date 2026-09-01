from typing import List, Optional
from matrix_model import MatrixInput, Ponto, MatrixResponse
 
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
