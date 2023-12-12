from pytz import timezone  # Coletando o timezone
from typing import Optional, List
from datetime import datetime, timedelta    # Coletando a data e hora
# Coletando o OAuth2PasswordBearer, Depends, HTTPException e status
from fastapi import  Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.future import select  # Coletando o select
from sqlalchemy.ext.asyncio import AsyncSession  # Coletando o AsyncSession

from jose import jwt  # Coletando o jwt

from models.usuario_model import UsuarioModel  # Coletando o UsuarioModel
from core.configs import settings  # Coletando o settings
from core.security import verificar_senha  # Coletando o verificar senha
from pydantic import EmailStr  # Coletando o EmailStr

# Criando um endpoint para verificar o token, que nos vamos usar para autenticar o usuário
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/usr/login"
)


async def autenticar(email: EmailStr, senha: str, db: AsyncSession) -> Optional[UsuarioModel]:

    async with db as sess:
        try:
            # Neste try, nos vamos verificar se o usuário existe no banco de dados e se a senha está correta
            query = select(UsuarioModel).filter(UsuarioModel.email == email)
            result = await sess.execute(query)
            usuario: UsuarioModel = result.scalar().unique().one_or_none()

            # Aqui ta bem simples, se o usuário não existir ou a senha estiver errada, vamos retornar None
            if not usuario:
                return None
            if not verificar_senha(senha, usuario.senha):
                return None
        except:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao autenticar o usuário")
        finally:
            return usuario


def cria_token(tipo_token: str, sub: str, expires_delta: Optional[timedelta] = None) -> str:
    payload = {}  # Criando um dicionario vazio
    zona = timezone('America/Sao_Paulo')  # Coletando o timezone
    data_expiracao = datetime.now(
        # Coletando a data e hora
        tz=zona) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    payload["type"] = tipo_token  # Adicionando o tipo de token no dicionario
    # Adicionando a data de expiração no dicionario
    payload["exp"] = data_expiracao
    # Adicionando a data de criação do token no dicionario
    payload['iat'] = datetime.now(tz=zona)
    payload['sub'] = str(sub)  # Adicionando o email do usuario no dicionario

    # Retornando o token
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)


def criar_token_acesso(email: str) -> str:
    # Retornando o token de acesso
    return cria_token("access_token", email, timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
