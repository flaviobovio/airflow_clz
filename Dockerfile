FROM apache/airflow:2.10.0

USER root

# Install dependencies
RUN apt-get update && \
    apt-get install -y unixodbc-dev curl gnupg && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17

USER airflow
RUN pip install pyodbc
