from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class MatrizInput(BaseModel):
    matriz: List[List[str]]


@app.post("/receber-matriz")
async def receber_matriz(dados: MatrizInput):
    """
    Recebe a matriz no seguinte formato:

    {
    "matrix": [
        ["R", ".", ".", "P"],
        [".", ".", ".", "."],
        ["P", ".", ".", "P"]
    ]
    }

    """
    linhas = len(dados.matriz)
    colunas = len(dados.matriz[0]) if linhas > 0 else 0
    return {"linhas": linhas, "colunas": colunas}

