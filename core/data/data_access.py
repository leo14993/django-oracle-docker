import redis
import pickle
import os
from src.configs.myproject_configs import Configs
config = Configs()


class RedisCacheService:

    def __init__(self, host, port, db, password):
        self.cache = redis.StrictRedis(
            host=host,
            port=port,
            db=db,
            password=password   
        )

    def set(self, key, value, serialization=False):
        if serialization:
            self.cache.set(key, pickle.dumps(value))
        else:
            self.cache.set(key, value)

    def get(self, key, serialization=False):
        result = self.cache.get(key)
        if serialization and result is not None:
            result = pickle.loads(result)
        return result

    def delete(self, key):
        return self.cache.delete(key)

    def flush(self):
        self.cache.flushall()

    def keys(self):
        return self.cache.keys()



redis_cache = RedisCacheService(
    host=config.REDIS_CACHE_HOST,
    port=config.REDIS_CACHE_PORT,
    db=config.REDIS_CACHE_DB,
    password=config.REDIS_CACHE_PASSWORD
)



def get_DATA_BASE():
    """
    parâmetro de saída:
        Dicionário com informações necessárias para conectar ao Banco de dados
    """
    # try:
    #     DATA_BASE = {
    #                 'ENGINE':os.getenv('DATABASE_ENGINE'),
    #                 'NAME': os.getenv('DATABASE_SERVICE'),
    #                 'HOST': os.getenv('DATABASE_HOST'),
    #                 'USER': os.getenv('DATABASE_USER'),
    #                 'PASSWORD': os.getenv('DATABASE_PASSWORD'),
    #                 'PORT': os.getenv('DATABASE_PORT')
    #                 }
    # except Exception as e:
    #     print(f"Erro: {e}. Usando o banco de dados sqlite")
    DATA_BASE = {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join('core/data/', 'myproject.sqlite3'),
                }
    return DATA_BASE

DATA_BASE= get_DATA_BASE()