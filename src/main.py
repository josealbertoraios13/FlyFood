from pathlib import Path

from routes import carregar_matrix

CAMINHO_JSON = Path(__file__).parent.parent / "matrix.json"

if __name__ == "__main__":
    resultado = carregar_matrix(CAMINHO_JSON)

    print(f"Rota: {resultado.rota}")
    print(f"Distância: {resultado.distancia} dronômetros")
    print(f"Tempo de resolução: {resultado.tempo_resolucao}s")