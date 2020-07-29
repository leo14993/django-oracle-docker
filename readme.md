# Backend de API Django REST com Conexão a banco de dados Oracle


## Pré-requisitos

Desenvolvido em: 
Linguagem de programação: Python 3.7
Bibliotecas: em `requirements.txt`
IDE: Visual Studio
Sistema Operacional: Windows 10

### Guia de instalação

1º Passo: Criar um ambiente virtual: `virtualenv my_env --no-download`

2º Passo: Ativar ambiente virtual: `myenv/Scripts/activate`

3º Passo: instalar as libs contidas no arquivo requirements.txt: `pip install -r requirements.txt`

4º Passo: Inicializar o servidor: `python manage.py runserver`
    * opcional: `python manage.py runserver {host}:{port}`, ex: `python manage.py runserver 0.0.0.0:7500`
    * caso utilizar servidor e porta opcional alterar as variavaveis de ambiente no arquivo `configmap-local.env`
    * alterar as variaveis `SERVER_API_HOST`e `PORT`
  
5º Fazer o pull da imagem redis no docker: `docker pull redis`

6º Instanciar o servidor no docker: docker run -p 6379:6379 redis redis-server --requirepass Your2020Redis
    * Se vc usa o docker para windows 10 Home, utilziando o docker Toolbox o host do container é `192.168.99.100`
    * Se for o docker de windows 10 pro, o host é o `localhost`ou `127.0.0.1`

#### Docker

Criar container:

*python:3.7-slim*
`docker build --no-cache --build-arg ENV=dev  --build-arg PORT=8000  --build-arg HOST=0.0.0.0  --build-arg SERVER_API_HOST=api-myproject.com.br  --build-arg DEBUG=FALSE  --build-arg SECRET_KEY=my_secretkey_123456789_django_Leonardo  --build-arg ALLOWED_HOSTS = ['127.0.0.1','api-myproject.com.br']  --build-arg DATABASE_ENGINE=django.db.backends.oracle  --build-arg DATABASE_NAME=Oracle_db_Name  --build-arg DATABASE_HOST=Oracle_host  --build-arg DATABASE_USER=Oracle_user  --build-arg DATABASE_PASSWORD=Oracle_password  --build-arg DATABASE_PORT=1521  --build-arg SERVICE_NAME=ORCL  --build-arg REDIS_CACHE_HOST=127.0.0.1  --build-arg REDIS_CACHE_PORT=6379  --build-arg REDIS_CACHE_DB=0  --build-arg REDIS_CACHE_PASSWORD=Your2020Redis  --build-arg IMG=python:3.7-slim  --build-arg STAGE='dev' -t myproject -f Dockerfile .`

*alpine:3.11*
`docker build --no-cache --build-arg ENV=dev  --build-arg PORT=8000  --build-arg HOST=0.0.0.0  --build-arg SERVER_API_HOST=api-myproject.com.br  --build-arg DEBUG=FALSE  --build-arg SECRET_KEY=my_secretkey_123456789_django_Leonardo  --build-arg ALLOWED_HOSTS = ['127.0.0.1','api-myproject.com.br']  --build-arg DATABASE_ENGINE=django.db.backends.oracle  --build-arg DATABASE_NAME=Oracle_db_Name  --build-arg DATABASE_HOST=Oracle_host  --build-arg DATABASE_USER=Oracle_user  --build-arg DATABASE_PASSWORD=Oracle_password  --build-arg DATABASE_PORT=1521  --build-arg SERVICE_NAME=ORCL  --build-arg REDIS_CACHE_HOST=127.0.0.1  --build-arg REDIS_CACHE_PORT=6379  --build-arg REDIS_CACHE_DB=0  --build-arg REDIS_CACHE_PASSWORD=Your2020Redis  --build-arg IMG=python:alpine:3.11  --build-arg STAGE='dev' -t myproject -f alpine.Dockerfile .`

Excecutar container:

`docker run -v <Source-path>:<container-path> -p <EXTERNAL-port>:<EXPOSE-port> <nome_do_container>`
`ex: docker run -v /c/DATABASE/:/app/base -p 8000:8000 myproject-backend-python  `

#### Python

Comandos para executar o projeto:
`python -m venv venv --clear`
`.venv\Scripts\activate`
`pip install --upgrade pip`
` pip install -r .\requirements.txt`
`python .\manage.py runserver 5000`

### Autoria e contribuições

· Desenvolvedor: Leonardo Rodrigues




