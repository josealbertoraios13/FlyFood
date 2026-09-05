from pydantic import BaseModel


class Ponto(BaseModel):
    x: int
    y: int