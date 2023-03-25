from __future__ import annotations

import datetime as dt

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.latest_only import LatestOnlyOperator

with DAG(
    dag_id="latest_onlywww",
    schedule=dt.timedelta(hours=4),
    start_date=dt.datetime(2021, 1, 1),
    catchup=False,
    tags=["example2", "example3"],
) as dag:
    latest_only = LatestOnlyOperator(task_id="latest_only")
    task1 = EmptyOperator(task_id="task1")

    latest_only >> task1

