from typing import List
from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.curso_model import CursoModel

from schemas.curso_schema import CursoSchema
from core.deps import get_session

router = APIRouter()

@router.post("/cursos", status_code=status.HTTP_201_CREATED, response_model=CursoSchema) # Aqui nos vamos inserir um curso no banco de dados
async def create_curso(curso: CursoSchema, session: AsyncSession = Depends(get_session)):
    try:
        curso_db = CursoModel(titulo=curso.titulo, descricao=curso.descricao, carga_horaria=curso.carga_horaria, preco=curso.preco)
        session.add(curso_db) # Aqui nos vamos adicionar o curso no banco de dados, mas nao vamos commitar ainda
        await session.commit() # Aqui nos vamos commitar o curso no banco de dados
        await session.refresh(curso_db)
    except:
        await session.rollback() # Aqui nos vamos dar rollback no curso no banco de dados
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao inserir o curso")
    finally:
        return curso_db

@router.get("/cursos", response_model=List[CursoSchema]) # E aqui vamos ler todos os cursos que estão no banco de dados
async def get_cursos(session: AsyncSession = Depends(get_session)):
    async with session as sess:
        query = select(CursoModel)
        result = await sess.execute(query)
        cursos: List[CursoModel] = result.scalars().all()
        
        return cursos

@router.get("/cursos/{curso_id}", response_model=CursoSchema) # Aqui nos vamos ler um curso especifico, que vamos coletar a partir do id transmitido
async def get_curso(curso_id: int, session: AsyncSession = Depends(get_session)):
    curso = await session.get(Curso, curso_id)
    if not curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
    return curso

@router.put("/cursos/{curso_id}", response_model=CursoSchema) # Aqui nos vamos atualizar um curso especifico, que vamos coletar a partir do id transmitido
async def update_curso(curso_id: int, curso: CursoSchema, session: AsyncSession = Depends(get_session)):
    async with session:
        query = select(CursoModel).where(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_db: CursoModel = result.scalar_one_or_none()
        
        if not curso_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
        else:
            try:
                curso_db.titulo = curso.titulo
                curso_db.descricao = curso.descricao
                curso_db.carga_horaria = curso.carga_horaria
                curso_db.preco = curso.preco
                await session.commit()
                await session.refresh(curso_db)
            except:
                await session.rollback()
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao atualizar o curso")
            finally:
                return curso_db

@router.delete("/cursos/{curso_id}", status_code=status.HTTP_204_NO_CONTENT) # Aqui nos vamos deletar um curso especifico, que vamos coletar a partir do id transmitido
async def delete_curso(curso_id: int, session: AsyncSession = Depends(get_session)):
    async with session:
        query = select(CursoModel).where(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_db: CursoModel = result.scalar_one_or_none()
        
        if not curso_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
        else:
            try:
                await session.delete(curso_db)
                await session.commit()
            except:
                await session.rollback()
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao deletar o curso")
            finally:
                return Response(status_code=status.HTTP_204_NO_CONTENT)


# Porque nos nao temos um endpoint para deletar todos os cursos? Porque nos nao vamos deletar todos os cursos, isso não faz sentido, mas se voce quiser, voce pode criar um endpoint para isso, mas isso não é recomendável em nenhuma hipótese, porque isso pode causar problemas no seu banco de dados, e isso pode causar problemas no seu sistema, e isso pode causar problemas no seu servidor, e isso pode causar problemas no seu computador, e isso pode causar problemas na sua vida, e isso pode causar problemas no seu universo...vc entendeu a ideia, né?


