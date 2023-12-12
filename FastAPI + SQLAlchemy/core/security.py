from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Criando uma classe para criptografar e comparar senhas
def verificar_senha(senha, senha_hash) -> bool:
    """Verifica se a senha e igual ao hash da senha"""
    return CRIPTO.verify(senha, senha_hash)


# Criando uma classe para gerar um hash da senha
def gerar_hash_senha(senha) -> str:
    """Gera um hash da senha"""
    return CRIPTO.hash(senha)
