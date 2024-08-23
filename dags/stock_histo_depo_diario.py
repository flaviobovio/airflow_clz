from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import pymssql
from datetime import datetime, timedelta
from functions.connections import ms_sql


# Define the DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=10),
    'start_date': datetime(2024, 8, 24, 2),
}

dag = DAG(
    'stock_histo_depo_diario',
    default_args=default_args,
    description='Guarda stock histórico diario x depósito',
    schedule_interval='0 4 * * *', # 04:00 AM
    start_date=days_ago(1),
    catchup=False,
)


def guarda_stock_diario():
    
    conn = pymssql.connect(**ms_sql())
    cursor = conn.cursor()

    # Check previous data does no exist 
    query = """
        SELECT COUNT(*), CAST(GETDATE() AS DATE)
            FROM omicronvt.dbo.t_stock_histo_depo_diario
            WHERE fecha = CAST(GETDATE() AS DATE)
    """
    cursor.execute(query)
    results = cursor.fetchone()
    if results[0] > 0:
        raise Exception(f'Ya existen registros con fecha {results[1]}')


    # Insert data
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
