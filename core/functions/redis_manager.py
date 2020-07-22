from core.data.data_access import redis_cache

def atualiza_cache(dados,chave):
    

    redis_cache.set(key=chave, value=dados, serialization=True)
    return(f"dados criados!")

def obter_cache(chave):
    
    dados = redis_cache.get(key=chave, serialization=True)})
    return(f"dados: {dados}")