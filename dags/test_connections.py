from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import pymssql
import pymysql
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
        print("Connection to MS SQL Server successful!")
        connection.close()
    except pymssql.DatabaseError as e:
        print(f"Database connection to MS SQL Server failed: {e}")
    except Exception as e:
        print(f"An error occurred connecting to MySQL Server: {e}")


def test_mssql():
    try:
        # Establish the connection
        connection = pymysql.connect(**connections.my_sql())
        # Connection successful if no exception is raised
        print("Connection to MySQL Server successful!")
        connection.close()
    except pymssql.DatabaseError as e:
        print(f"Database connection to MySQL Server failed: {e}")
    except Exception as e:
        print(f"An error occurred connecting to MySQL Server : {e}")




dag = DAG(
    'sql_connections_tests',
    default_args=default_args,
    description='Test connections to MS SQL & MySQL',
    schedule_interval='@once',
    start_date=days_ago(1),    
)

test_mssql = PythonOperator(
    task_id='test_mssql_connection',
    python_callable=test_mssql,
    dag=dag,
)


test_mysql = PythonOperator(
    task_id='test_mysql_connection',
    python_callable=test_mysql,
    dag=dag,
)




test_mssql >> test_mysql
