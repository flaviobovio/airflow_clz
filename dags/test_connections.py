from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
import pymssql
from functions import connections



# Define the DAG
default_args = {
    'owner': 'airflow',
    'retries': 0,
    #'retry_delay': timedelta(minutes=10),
}


def test_mssql():
    try:
        # Establish the connection
        connection = pymssql.connect(**connections.ms_sql())
        # Connection successful if no exception is raised
        print("Connection successful!")
        connection.close()
    except pymssql.DatabaseError as e:
        print(f"Database connection failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


dag = DAG(
    'mssql_test',
    default_args=default_args,
    description='Test connection to MS SQL Server',
    schedule_interval='@once',    
)

test_mssql = PythonOperator(
    task_id='test_mssql_connection',
    python_callable=test_mssql,
    dag=dag,
)

test_mssql
