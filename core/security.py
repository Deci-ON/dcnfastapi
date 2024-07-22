from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verificar_senha(senha: str, hash_senha: str) -> bool:
    """
    Verifica se a senha esta correta, comparando a senha em texto puro, infomada pelo usuario.
    """
    return CRIPTO.verify(senha, hash_senha)


def gerar_hash_senha(senha: str) -> str:
    """
    Gera e retorna hash da senha
    """
    return CRIPTO.hash(senha)