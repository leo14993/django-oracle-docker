# Imagem do container para dockerização do projeto Valvulas
FROM python:3.7-slim

MAINTAINER Leonardo Rodrigues
# Variáveis de ambiente

RUN apt-get update -y && apt-get install alien -y


COPY  requirements.txt /app/
COPY . /app

WORKDIR /app

ARG PORT
ARG HOST 
ARG DB_USER
ARG DB_PASSWORD
ARG DB_HOST
ARG DB_PORT
ARG DB_SERVICE
ARG DEBUG

# Define environment variable
ENV PORT=${PORT}
ENV HOST=${HOST}
ENV DEBUG_MODE=${DEBUG}
ENV DB_USER=${DB_USER}
ENV DB_PASSWORD=${DB_PASSWORD}
ENV DB_HOST=${DB_HOST}
ENV DB_PORT=${DB_PORT}
ENV DB_SERVICE=${DB_SERVICE}

# get and install oracle aplications 
ADD https://download.oracle.com/otn_software/linux/instantclient/195000/oracle-instantclient19.5-basiclite-19.5.0.0.0-1.x86_64.rpm ./instantclient19.5-basiclite.rpm

RUN alien -i  --scripts  ./instantclient19.5-basiclite.rpm && rm ./instantclient19.5-basiclite.*

RUN pip install -r requirements.txt && apt-get install libaio1 libaio-dev -y && apt-get remove alien -y

ENV LD_LIBRARY_PATH="/usr/lib/oracle/19.5/client(64)/lib/${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
ENV ORACLE_HOME="/usr/lib/oracle/19.5/client(64)"
ENV PATH="/usr/lib/oracle/19.5/;"+${PATH}

#create user
RUN useradd python

# Copy the current directory contents into the container at /app
COPY --chown=python . /app

EXPOSE ${PORT}

USER python

CMD python manage.py makemigrations
CMD python manage.py migrate
CMD python manage.py runserver 0.0.0.0:${PORT}
