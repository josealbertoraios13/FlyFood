from fastapi import APIRouter, HTTPException
from model.matrix_model import (
    MatrixInput,
    MatrixResponse,
    RotasInput,
    MenorRotaResponse,
)

from services import matriz_para_pontos, encontrar_menor_rota

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "API está funcionando!"}


@router.post("/flyfood", response_model=MatrixResponse)
async def obter_pontos(dados: MatrixInput):
    """
    Endpoint para processar a matriz de entrada e retornar os pontos correspondentes.

    Exemplo de entrada:
    {
  "matrix": [
    [".", "I", ".", "P"],
    [".", ".", "P", "."],
    ["P", ".", ".", "."],
    [".", ".", "P", "."]
  ]
}
    """
    try:
        return matriz_para_pontos(dados.matrix)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/flyfood/menor-rota", response_model=MenorRotaResponse)
async def obter_menor_rota(dados: RotasInput):
    """
    Endpoint que recebe todas as possibilidades de rota (com a
    distância de cada uma), ordena pela distância e retorna o
    menor caminho junto com sua respectiva distância.

    Exemplo de entrada:
    {
      "rotas": [
        {"caminho": [{"x":0,"y":0}, {"x":1,"y":0}], "distancia": 25},
        {"caminho": [{"x":0,"y":0}, {"x":2,"y":0}], "distancia": 18}
      ]
    }
    """
    try:
        return encontrar_menor_rota(dados.rotas)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))