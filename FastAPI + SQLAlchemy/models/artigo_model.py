from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from core.configs import settings

class ArtigoModel(settings.DBBaseModel):
    __tablename__ = "artigos"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String)
    url_fonte: str = Column(String)
    conteudo: str = Column(String)
    usuario_id: int = Column(Integer, ForeignKey("usuarios.id"))

    criador = relationship("UsuarioModel", back_populates="artigos", lazy="joined")

    class Config:
        orm_mode = True

