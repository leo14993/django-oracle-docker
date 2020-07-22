ARG IMG=${IMG}
# python:3.7
FROM ${IMG}

# FROM python:3.6-alpine3.9

LABEL MAINTAINER "Leonardo Rodrigues <leonardo.rodrigues@spassu.com>"

ARG ENV

ARG STAGE
ARG PORT=8000
ARG HOST 
ARG DEBUG

ENV STAGE=${STAGE}
ENV DEBUG=${DEBUG}
ENV PORT=${PORT}
ENV HOST=${HOST}

#ARGS do PI WEB SERVICE
ARG PI_WEB_API_USER
ARG PI_WEB_API_PASSWORD
ARG PI_WEB_API_SERVER
ARG PI_WEB_API_PATH
ARG PI_WEB_API_VERIFY

# Variaveis ambiente PI
ENV PI_WEB_API_USER=${PI_WEB_API_USER}
ENV PI_WEB_API_PASSWORD=${PI_WEB_API_PASSWORD}
ENV PI_WEB_API_SERVER=${PI_WEB_API_SERVER}
ENV PI_WEB_API_PATH=${PI_WEB_API_PATH}
ENV PI_WEB_API_VERIFY=${PI_WEB_API_VERIFY}

#Instalando Python e suas dependencias
RUN apk add --no-cache python3 py3-pip python3-dev 

#Copiando arquivos
COPY . /app
#Definindo local de trabalho
WORKDIR /app

#Criando grupo de usuarios e usuario com poderes limitados
RUN addgroup appgroup 
RUN adduser python -D appgroup

# Instalando libs necessarias para execucao da API
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

#Libs necessarias para funcionamento do ML
RUN apk add --no-cache cmake gcc libxml2 automake g++ libxml2-dev libxslt-dev lapack-dev gfortran

# Instalando libs necessarias para execucao do modelo ML
RUN pip install wheel
RUN pip install -r requirements_ML.txt

RUN pip install --force-reinstall --no-cache fbprophet 

COPY --chown=python . /app

EXPOSE ${PORT}

USER python

# CMD python3 pSchedule.py & 
CMD python3 manage.py runserver ${HOST}:${PORT} 


