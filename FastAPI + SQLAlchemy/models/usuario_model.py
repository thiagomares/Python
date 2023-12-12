from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from core.configs import settings


class UsuarioModel(settings.DBBaseModel):
    __tablename__ = "usuarios"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String)
    email: str = Column(String)
    senha: str = Column(String)
    ativo: bool = Column(Boolean, default=True)

    artigos = relationship("ArtigoModel", back_populates="criador",
                           lazy="joined", cascade="all, delete-orphan", uselist=True)
