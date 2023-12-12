from typing import Optional
from pydantic import BaseModel as SCBaseModel, HttpUrl

class ArtigoSchema(SCBaseModel):

    titulo: str
    url_fonte: HttpUrl
    conteudo: str
    usuario_id: Optional[int]
    
    class Config:
        orm_mode = True