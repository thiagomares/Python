from core.configs import settings
from sqlalchemy import Column, Integer, String, Float

class CursoModel(settings.DBBaseModel):
    __tablename__ = "cursos"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String)
    descricao: str = Column(String)
    carga_horaria: int = Column(Integer)
    preco: float = Column(Float)
