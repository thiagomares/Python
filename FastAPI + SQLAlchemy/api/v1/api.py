from fastapi import APIRouter

from api.v1.endpoints import curso, artigo, usuario

api_router = APIRouter()
api_router.include_router(curso.router, tags=["cursos"]) # Aqui nos vamos incluir o router do curso na api_router, com o prefixo /cursos e a tag cursos
api_router.include_router(artigo.router, tags=["artigo"])
api_router.include_router(usuario.router,prefix="/user", tags=["usuario"])
