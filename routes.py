from fastapi import APIRouter, HTTPException
from matrix_model import MatrixInput, MatrixResponse
 
from services import matriz_para_pontos
 
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
