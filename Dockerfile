# ARG IMG=nexus.petrobras.com.br:5000/library/python:3.7
ARG IMG=${IMG}
# python:3.7
FROM ${IMG}
# FROM python:3.8.3-slim
# FROM python:3.9-rc-buster

LABEL MAINTAINER "Leonardo Rodrigues <leonardo.rodrigues@spassu.com>"

COPY . /app
WORKDIR /app

#API config
ARG ENV

ARG PORT=8000
ARG HOST 
ARG SERVER_API_HOST
ARG SERVER_API_PORT
ARG DEBUG
ARG SECRET_KEY
ARG ALLOWED_HOSTS

ENV ENV=${ENV}
ENV PORT=${PORT}
ENV HOST=${HOST}
ENV SERVER_API_HOST=${SERVER_API_HOST}
ENV SERVER_API_PORT=${SERVER_API_PORT}
ENV DEBUG=${DEBUG}
ENV SECRET_KEY=${SECRET_KEY}
ARG ALLOWED_HOSTS=${ALLOWED_HOSTS}


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

#ARGS BD Oracle
ARG DATABASE_ENGINE
ARG DATABASE_NAME
ARG DATABASE_HOST
ARG DATABASE_USER
ARG DATABASE_PASSWORD
ARG DATABASE_PORT
ARG SERVICE_NAME

#Variáveis de Ambiente BD Oracle
ENV DATABASE_ENGINE=${DATABASE_ENGINE} 
ENV DATABASE_NAME=${DATABASE_NAME} 
ENV DATABASE_HOST=${DATABASE_HOST} 
ENV DATABASE_USER=${DATABASE_USER} 
ENV DATABASE_PASSWORD=${DATABASE_PASSWORD} 
ENV DATABASE_PORT=${DATABASE_PORT} 
ENV SERVICE_NAME=${SERVICE_NAME} 

#ARGS Cache Redis
ARG REDIS_CACHE_HOST
ARG REDIS_CACHE_PORT
ARG REDIS_CACHE_DB
ARG REDIS_CACHE_PASSWORD

#Variáveis de Ambiente Cache Redis
ENV REDIS_CACHE_HOST=${REDIS_CACHE_HOST}
ENV REDIS_CACHE_PORT=${REDIS_CACHE_PORT}
ENV REDIS_CACHE_DB=${REDIS_CACHE_DB}
ENV REDIS_CACHE_PASSWORD=${REDIS_CACHE_PASSWORD}

#baixa e instala os drives da oracle, redis e instala os requirements
ADD https://download.oracle.com/otn_software/linux/instantclient/195000/oracle-instantclient19.5-basiclite-19.5.0.0.0-1.x86_64.rpm ./instantclient19.5-basiclite.rpm

RUN apt-get update -y && \
apt-get upgrade -y && \
apt-get install alien perl -y && \
apt-get install -y redis-server && \
apt-get install gcc g++ -y && \
alien -i --scripts  ./instantclient19.5-basiclite.rpm && \
pip install --upgrade pip && pip install -r  requirements.txt && \
pip install --force-reinstall --no-cache -r requirements_ML.txt && \
apt-get install  libaio-dev -y && \
apt-get remove alien -y && \
useradd python

ENV LD_LIBRARY_PATH="/usr/lib/oracle/19.5/client(64)/lib/${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
ENV ORACLE_HOME="/usr/lib/oracle/19.5/client(64)"
ENV PATH="/usr/lib/oracle/19.5/;"+${PATH}



# install all the specific requirements for a state
# RUN sh requirements.sh ${STAGE}

# RUN apt-get update -y && \
# apt-get install gcc g++ -y
# RUN pip install --upgrade pip &&  pip install -r requirements.txt 
# RUN  pip install --force-reinstall --no-cache -r requirements_ML.txt 
# RUN apt-get remove gcc g++ -y 


COPY --chown=python . /app

EXPOSE ${PORT}

USER python

CMD redis-server --requirepass Your2020Redis --daemonize yes && python background.py & python manage.py runserver ${HOST}:${PORT} 



