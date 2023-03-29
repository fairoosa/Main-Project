import datetime as dt

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python_operator import PythonOperator


def middle_task():
    print("AIRFLOW IN PROGRESS")
    


with DAG(
    dag_id = "scrapper",
    schedule_interval = '@once',
    start_date=dt.datetime(2021, 1, 1),
    catchup=False,
) as dag:
    task1 = EmptyOperator(task_id = "start")
    task2 = PythonOperator(task_id = "middle", python_callable = middle_task)
    task3 = EmptyOperator(task_id = "end")

    task1 >> task2 >> task3



