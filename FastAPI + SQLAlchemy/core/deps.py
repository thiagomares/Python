from typing import Generator, Optional
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel, EmailStr
from core.database import Session as Sesssion
from models.usuario_model import UsuarioModel
from core.auth import oauth2_scheme
from core.configs import settings


async def get_session() -> Generator:
    session: AsyncSession = Sesssion()
    try:
        yield session
    finally:
        await session.close()


class TokenData(BaseModel):
    email: Optional[EmailStr] = None


async def get_current_user(token: str = Depends(oauth2_scheme), session: AsyncSession = Depends(get_session)) -> UsuarioModel:
    try:
        """No try, nos vamos decodificar o token e verificar se o usuário que estamos testando tem dados no banco de dados"""
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[
                             settings.ALGORITHM], options={"verify_aud": False})
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
        token_data = TokenData(email=username)

        async with session as sess:
            query = select(UsuarioModel).filter(
                UsuarioModel.id == int(token_data.id))
            result = await sess.execute(query)
            usuario: UsuarioModel = result.scalars().unique().one_or_none()

    except JWTError:
        # Se por algum motivo o token for invalido, vamos retornar um erro
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
    except:
        # Se por algum motivo der erro, vamos retornar um erro
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Erro ao autenticar o usuário")
    finally:
        if not usuario:
            # Se por algum motivo o usuario não for encontrado, vamos retornar um erro
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
        return usuario


async def get_current_active_user(current_user: UsuarioModel = Depends(get_current_user)) -> UsuarioModel:
    if not current_user.ativo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Usuário inativo")
    return current_user
