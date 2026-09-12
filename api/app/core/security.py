import bcrypt

#Gera um salt aleatorio e cria o hash seguro da senha usando bcrypt.   
def hash_senha(senha: str) -> str:
    # Hash a senha usando o algoritmo bcrypt.
    return bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
