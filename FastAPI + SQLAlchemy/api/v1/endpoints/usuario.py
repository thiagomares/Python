from typing import List, Optional, Any

from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

from models.usuario_model import UsuarioModel
from schemas.usuario_schema import UsuarioSchemaBase, UsuarioSchemaCreate, UsuarioSchemaUpdate
from core.deps import get_session, get_current_user
from core.security import gerar_hash_senha
from core.auth import autenticar, criar_token_acesso

router = APIRouter()

# Get Logon
@router.post("/login", response_model=UsuarioSchemaBase)
def get_logado(usuario_logado: UsuarioSchemaBase = Depends(get_current_user)):
    return usuario_logado

# Sign Up
@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=UsuarioSchemaBase)
async def create_usuario(usuario: UsuarioSchemaCreate, session: AsyncSession = Depends(get_session)):
    try:
        async with session as sess:
            usuario_db = UsuarioModel(nome=usuario.nome, email=usuario.email, senha=gerar_hash_senha(usuario.senha))
            sess.add(usuario_db)
            await sess.commit()
            await sess.refresh(usuario_db)
            return usuario_db
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Usuário já cadastrado")
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao inserir o usuário")

    
# Get All
@router.get("/usuarios", response_model=List[UsuarioSchemaBase])
async def get_usuarios(session: AsyncSession = Depends(get_session)):
    try:
        async with session as sess:
            query = select(UsuarioModel)
            result = await sess.execute(query)
            usuarios = result.scalars().unique().all()
            return usuarios
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao buscar os usuários")
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao buscar os usuários")

# Get One
@router.get("/usuarios/{usuario_id}", response_model=UsuarioSchemaBase)
async def get_usuario(usuario_id: int, session: AsyncSession = Depends(get_session)):
    try:
        async with session as sess:
            query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
            result = await sess.execute(query)
            usuario = result.scalars().unique().one_or_none()
            if not usuario:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
            return usuario
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao buscar o usuário")
    


# Update
@router.put("/usuarios/{usuario_id}", response_model=UsuarioSchemaBase)
async def update_usuario(usuario_id: int, usuario: UsuarioSchemaUpdate, session: AsyncSession = Depends(get_session)):
    try:
        async with session as sess:
            query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
            result = await sess.execute(query)
            usuario_db: UsuarioModel = result.scalars().unique().one_or_none()
            if not usuario_db:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
            else:
                try:
                    usuario_db.nome = usuario.nome
                    usuario_db.email = usuario.email
                    usuario_db.senha = gerar_hash_senha(usuario.senha)
                    await sess.commit()
                    await sess.refresh(usuario_db)
                except IntegrityError:
                    await sess.rollback()
                    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao atualizar o usuário")
                finally:
                    return usuario_db
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao atualizar o usuário")