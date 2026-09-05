from fastapi import APIRouter, HTTPException

from model import MatrixInput, MenorCaminhoResponse
from services import processar_matrix

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "API está funcionando!"}


@router.post("/flyfood", response_model=MenorCaminhoResponse)
async def obter_pontos(dados: MatrixInput) -> MenorCaminhoResponse:
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

    print("Davi")
    try:
        return processar_matrix(dados.matrix)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))