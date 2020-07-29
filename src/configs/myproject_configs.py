import base64 , json
import os
import ast
from core.functions.suport import Functions
from dotenv import load_dotenv, find_dotenv
from datetime import datetime

ENV = os.getenv("ENV")

if ENV==None or ENV.lower()=="local":
    env = "configmap-local.env"
    protocol = "http://"
else:
    env = f"configmap-{ENV.lower()}.env"
    protocol = "https://"


dotenv_path = os.path.join('', env)
load_dotenv(dotenv_path)


class Configs:  

    def __init__(self):
         
        
        self.ALLOWED_HOSTS = ast.literal_eval(os.getenv("ALLOWED_HOSTS"))
        self.DEBUG = Functions.boolean(os.getenv("DEBUG"))
        self.SECRET_KEY = os.getenv('SECRET_KEY')
        self.REDIS_CACHE_HOST=os.getenv('REDIS_CACHE_HOST')
        self.REDIS_CACHE_PORT=os.getenv('REDIS_CACHE_PORT')
        self.REDIS_CACHE_DB=os.getenv('REDIS_CACHE_DB')
        self.REDIS_CACHE_PASSWORD=os.getenv('REDIS_CACHE_PASSWORD')
        self.PI_WEB_API_USER=os.getenv('PI_WEB_API_USER')
        self.PI_WEB_API_PASSWORD= os.getenv('PI_WEB_API_PASSWORD')
        self.PI_WEB_API_B64_USER_PASSWORD = base64.b64encode(bytes(f"{self.PI_WEB_API_USER}:{self.PI_WEB_API_PASSWORD}", 'utf-8')).decode("utf-8")   
        self.PI_WEB_API_AUTH_HEADERS =  {"Content-Type": "application/json; charset=UTF-8"
                                        ,"X-Requested-With":"worked"
                                        , "Authorization":f"Basic {self.PI_WEB_API_B64_USER_PASSWORD}"}


class endpoints(object):
    
    HOME = 'home'
    HEALTH = 'health'
    CREATE_PROJECT = 'project/create'
    MY_PROJECT = 'project'
    UPDATE_MY_PROJECT = "project/update"
    

class redirect(object):
    
    PORT = os.getenv("PORT")
    SERVER_API_HOST = Functions.validate_url(host=os.getenv("SERVER_API_HOST"), protocol=protocol)
    HOST = f"{SERVER_API_HOST}:{PORT}"
    HOME = f"{HOST}/{endpoints.HOME}"
    HEALTH = f"{HOST}/{endpoints.HEALTH}"
    CREATE_PROJECT = f"{HOST}/{endpoints.CREATE_PROJECT}"
    MY_PROJECT = f"{HOST}/{endpoints.MY_PROJECT}"
    UPDATE_MY_PROJECT = f"{HOST}/{endpoints.UPDATE_MY_PROJECT}"

