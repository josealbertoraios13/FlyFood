import json
from pathlib import Path

from model import MatrixInput, MenorCaminhoResponse
from services import processar_matrix


def carregar_matrix(caminho_arquivo: str | Path) -> MenorCaminhoResponse:
    """
    Lê o arquivo JSON com a matriz, valida o formato e devolve o menor caminho.

    Exemplo de arquivo:
    [
      ["R", ".", ".", "A"],
      [".", ".", "B", "."],
      [".", "C", ".", "."],
      [".", ".", ".", "D"]
    ]
    """

    caminho = Path(caminho_arquivo)

    with caminho.open(encoding="utf-8") as arquivo:
        dados_json = json.load(arquivo)

    dados = MatrixInput(matrix=dados_json)

    return processar_matrix(dados.matrix)
