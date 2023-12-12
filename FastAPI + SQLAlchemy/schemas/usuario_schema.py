from typing import Optional, List
from pydantic import BaseModel as SCBaseModel, EmailStr

from schemas.artigo_schema import ArtigoSchema

class UsuarioSchemaBase(SCBaseModel):

    nome: str
    email: EmailStr
    ativo: Optional[bool] = True
    

    class Config:
        orm_mode = True
        
class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str
    
class UsuarioSchemaArtigos(UsuarioSchemaBase):
    artigos: Optional[List[ArtigoSchema]]
    
class UsuarioSchemaUpdate(UsuarioSchemaBase):
    senha: Optional[str]
    nome: Optional[str]
    email: Optional[EmailStr]
    ativo: Optional[bool]
    
