from airflow import DAG
from airflow.operators.python import PythonOperator  # Updated import for PythonOperator
from datetime import datetime
import pyodbc

def connect_to_mssql():
    conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=your_server;DATABASE=your_database;UID=your_user;PWD=your_password'
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM your_table')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 8, 1),
    'retries': 0,
}

dag = DAG(
    'mssql_example',
    default_args=default_args,
    description='A simple MS SQL Server example',
    schedule_interval=None,
    catchup=False  # Ensure the DAG doesn't backfill old runs
)

t1 = PythonOperator(
    task_id='connect_to_mssql',
    python_callable=connect_to_mssql,
    dag=dag,
)


t1