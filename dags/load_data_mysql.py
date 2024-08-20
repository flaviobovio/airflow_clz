from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.utils.dates import days_ago
import mysql.connector
import pandas as pd
from datetime import timedelta

# DB Conection parameters
cnx_host = '172.17.0.1'
cnx_user = 'root'
cnx_password = 'password'
cnx_database = 'calzalindo'

# Define the DAG
default_args = {
    'owner': 'airflow',
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'load_data_to_mysql',
    default_args=default_args,
    description='Load data into MySQL',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
)

# # Function to fetch data (this could be modified to get data from any source, e.g., an API or CSV)
# def fetch_data(**kwargs):
#     # Simulating data fetch, this can be replaced with actual data fetch logic (like pandas read_csv, API calls)
#     data = pd.DataFrame({
#         'id': [1, 2, 3],
#         'name': ['John', 'Jane', 'Doe'],
#         'age': [23, 25, 30]
#     })
#     # Save the data as CSV for now (or handle it differently)
#     data.to_csv('/tmp/fetched_data.csv', index=False)

# # Python operator to fetch data
# fetch_data_task = PythonOperator(
#     task_id='fetch_data',
#     python_callable=fetch_data,
#     dag=dag,
# )

# Function to load data into MySQL
def load_data_to_mysql(**kwargs):
    # Connect to MySQL
    conn = mysql.connector.connect(
        host=cnx_host,
        user=cnx_user,
        password=cnx_password,
        database=cnx_database
    )
    
    cursor = conn.cursor()
    
    # Load the CSV data into a pandas DataFrame
    data = pd.read_csv('dags/data/prueba.csv')

    # Transform data
    data['first_name'] = data['last_name'] + ' ' + data['first_name']
    data.rename(columns={'first_name':'name'})
    data.drop(columns=['last_name'], inplace=True)
    data['gender'] = data['gender'].apply(lambda x : x[:1])
    
    # Insert data into MySQL table
    for i, row in data.iterrows():
        print(tuple(row))
        sql = "INSERT INTO clientes (id, name, email, gender) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, tuple(row))
    
    # Commit and close
    conn.commit()
    cursor.close()
    conn.close()

# Python operator to load data into MySQL
load_data_task = PythonOperator(
    task_id='load_data_to_mysql',
    python_callable=load_data_to_mysql,
    dag=dag,
)

# Set task dependencies
#fetch_data_task >> load_data_task
load_data_task
