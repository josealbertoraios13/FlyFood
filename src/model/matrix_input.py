import string

from pydantic import BaseModel, field_validator

VALORES_VALIDOS = set(string.ascii_uppercase) | {"0"}

class MatrixInput(BaseModel):
    matrix: list[list[str]]

    @field_validator("matrix")
    @classmethod
    def validate_matrix(cls, value):
        if not value or not value[0]:
            raise ValueError("A matriz não pode estar vazia.")

        largura = len(value[0])

        if any(len(linha) != largura for linha in value):
            raise ValueError("Todas as linhas da matriz devem ter o mesmo tamanho.")


        for linha in value:
            for celula in linha:
                if str(celula).strip().upper() not in VALORES_VALIDOS:
                    raise ValueError(
                        f"Valor inválido na matriz: '{celula}'. Use 'R', uma letra de 'A' a 'Z' ou '0'."
                    )

        return value