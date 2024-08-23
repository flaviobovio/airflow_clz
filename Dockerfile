FROM apache/airflow:2.10.0

# Set environment variables
ENV AIRFLOW__WEBSERVER__EXPOSE_CONFIG=True
ENV AIRFLOW__CORE__TEST_CONNECTION=Enabled

USER root

#update package list
RUN apt update 

#install fretds for MSSQL
RUN apt install freetds-bin 

#install ping and telnet for debugging
RUN apt install iputils-ping telnet

USER airflow

# MSSQL
RUN pip install apache-airflow-providers-microsoft-mssql pymssql

# MySQL 
RUN pip install pymysql
