from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import pymssql
from datetime import timedelta
from .functions import connections


# Define the DAG
default_args = {
    'owner': 'airflow',
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'stock_histo_depo_diario',
    default_args=default_args,
    description='Guarda stock histórico diario x depósito',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
)


def guarda_stock_diario():
    
    conn = pymssql.connect(**connections.ms_sql())
    cursor = conn.cursor()
    query = """
        INSERT INTO omicronvt.dbo.t_stock_histo_depo_diario 
        SELECT deposito
            , SUM(stock_actual) as stock
            , CAST(GETDATE() AS DATE) AS fecha 
        FROM msgestionC.dbo.stock 
        GROUP BY deposito
    """
    cursor.execute(query)

    # Commit & close connection
    conn.commit()
    conn.close()




# Python operator to load data into MySQL
guarda_stock_diario = PythonOperator(
    task_id='guarda_stock_diario',
    python_callable=guarda_stock_diario,
    dag=dag,
)

guarda_stock_diario
