from typing import Optional
from pydantic import BaseModel as SCBaseModel

class CursoSchema(SCBaseModel):
    titulo: str
    descricao: str
    carga_horaria: int
    preco: float

    class Config:
        orm_mode = True
        