FROM python:3.6-slim
ENV TERM linux

# Airflow  # Locate Workflow Logic
ARG AIRFLOW_VERSION=1.8.0
ARG AIRFLOW_HOME=/usr/local/airflow
ARG APP_HOME=/usr/local/app_home

# Define en_US.
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8
ENV LC_MESSAGES en_US.UTF-8

COPY ./sql ${AIRFLOW_HOME}/sql
COPY ./dags ${AIRFLOW_HOME}/dags
COPY ./requirements.txt /requirements.txt

VOLUME ./dags:/usr/local/airflow/dags
VOLUME ./sql:/usr/local/airflow/sql

ENV CONFIG="PRODUCTION"

EXPOSE 8080 5555 8793

WORKDIR ${AIRFLOW_HOME}
