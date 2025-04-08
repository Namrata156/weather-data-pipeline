from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from scripts.extract import get_multiple_cities_weather
from scripts.transform import transform_weather_data
from scripts.load import save_to_postgres

# Default DAG settings
default_args = {
    'owner': 'namrata',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    dag_id='weather_etl_dag',
    default_args=default_args,
    description='ETL pipeline for weather data',
    start_date=datetime(2025, 4, 7),
    schedule_interval='@daily',
    catchup=False
) as dag:

    def extract():
        cities = ["Los Angeles", "San Francisco", "Bangalore"]
        return get_multiple_cities_weather(cities)

    def transform(ti):
        raw_data = ti.xcom_pull(task_ids='extract_task')
        df = transform_weather_data(raw_data)
        ti.xcom_push(key='transformed_df', value=df.to_json())  # pass DataFrame as JSON

    def load(ti):
        import pandas as pd
        df_json = ti.xcom_pull(task_ids='transform_task', key='transformed_df')
        df = pd.read_json(df_json)
        save_to_postgres(df)

    extract_task = PythonOperator(
        task_id='extract_task',
        python_callable=extract
    )

    transform_task = PythonOperator(
        task_id='transform_task',
        python_callable=transform
    )

    load_task = PythonOperator(
        task_id='load_task',
        python_callable=load
    )

    extract_task >> transform_task >> load_task