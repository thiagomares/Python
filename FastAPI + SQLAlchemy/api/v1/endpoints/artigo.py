from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.artigo_model import ArtigoModel
from models.usuario_model import UsuarioModel
from schemas.artigo_schema import ArtigoSchema
# Nos vamos usar o get_current_user para pegar o usuario logado, pois é nele que está guardado o token de acesso
from core.deps import get_session, get_current_user


router = APIRouter()

# Método Post


@router.post("/artigo", status_code=status.HTTP_201_CREATED, response_model=ArtigoSchema)
# Quando usamos o Depends, o FastAPI vai chamar a função get_session e passar o resultado dela para a função create_artigo,  e o mesmo acontece com o current_user, e temos que ter certeza que o nosso usuário existe, logo, devemos passar o current_user como dependencia
async def create_artigo(artigo: ArtigoSchema, session: AsyncSession = Depends(get_session), current_user: UsuarioModel = Depends(get_current_user)):
    try:
        async with session as sess:
            novo_artigo = ArtigoModel(titulo=artigo.titulo, conteudo=artigo.conteudo,
                                      autor_id=current_user.id, url_fonte=artigo.url_fonte)
            sess.add(novo_artigo)
            await sess.commit()
            await sess.refresh(novo_artigo)
            return novo_artigo
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao criar o artigo")


# Método Get
@router.get("/artigo", response_model=List[ArtigoSchema])
async def get_artigos(session: AsyncSession = Depends(get_session)):
    try:
        async with session as sess:
            query = select(ArtigoModel)
            result = await sess.execute(query)
            artigos = result.scalars().unique().all()
            return artigos
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao buscar os artigos")

# Método Get com ID
@router.get("/artigo/{artigo_id}", response_model=ArtigoSchema)
async def get_artigo(artigo_id: int, session: AsyncSession = Depends(get_session)):
    try:
        async with session as sess:
            query = select(ArtigoModel).filter(ArtigoModel.id == artigo_id)
            result = await sess.execute(query)
            artigo = result.scalars().unique().one_or_none()
            if not artigo:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="Artigo não encontrado")
            return artigo
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao buscar o artigo")

# Método Put
@router.put("/artigo/{artigo_id}", response_model=ArtigoSchema)
async def update_artigo(artigo_id: int, artigo: ArtigoSchema, session: AsyncSession = Depends(get_session), current_user: UsuarioModel = Depends(get_current_user)):
    try:
        async with session as sess:
            query = select(ArtigoModel).filter(ArtigoModel.id == artigo_id).filter(curent_user.id == ArtigoModel.autor_id)
            result = await sess.execute(query)
            artigo_bd = result.scalars().unique().one_or_none()
            if not artigo_bd:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="Artigo não encontrado")
            if artigo_bd.autor_id != current_user.id:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                    detail="Você não tem permissão para editar esse artigo")
            artigo_bd.titulo = artigo.titulo
            artigo_bd.conteudo = artigo.conteudo
            artigo_bd.url_fonte = artigo.url_fonte
            await sess.commit()
            await sess.refresh(artigo_bd)
            return artigo_bd
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao atualizar o artigo")

# Método Delete
@router.delete("/artigo/{artigo_id}")
async def delete_artigo(artigo_id: int, session: AsyncSession = Depends(get_session), current_user: UsuarioModel = Depends(get_current_user)):
    try:
        async with session as sess:
            query = select(ArtigoModel).filter(ArtigoModel.id == artigo_id).filter(curent_user.id == ArtigoModel.autor_id)
            result = await sess.execute(query)
            artigo_bd = result.scalars().unique().one_or_none()
            if not artigo_bd:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="Artigo não encontrado")
            if artigo_bd.autor_id != current_user.id:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                    detail="Você não tem permissão para deletar esse artigo")
            await sess.delete(artigo_bd)
            await sess.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao deletar o artigo")
