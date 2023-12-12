from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router

app = FastAPI(title='Curso de FastAPI', version='0.0.1')
# Aqui nos vamos incluir o api_router na app, com o prefixo /api/v1
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn
    # Aqui nos vamos rodar a app com o uvicorn, na porta 8000, com o log_level info e com o reload True
    uvicorn.run("main:app", host='localhost', port=8000,
                log_level='info', reload=True)
