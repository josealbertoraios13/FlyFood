import json
from pathlib import Path

from model import MatrixInput, MenorCaminhoResponse
from services import processar_matrix


def carregar_matrix(caminho_arquivo: str) -> MenorCaminhoResponse:
    """
    Exemplo de arquivo:
    {
      "matrix": [
        [".", "R", ".", "A"],
        [".", ".", "B", "."],
        ["C", ".", ".", "."],
        [".", ".", "D", "."]
      ]
    }
    """

    caminho = Path(caminho_arquivo)

    with caminho.open(encoding="utf-8") as arquivo:
      dados_json = json.load(arquivo)

    dados = MatrixInput(**dados_json)

    return processar_matrix(dados.matrix)