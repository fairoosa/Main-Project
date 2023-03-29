

import datetime as dt

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python_operator import PythonOperator
from bs4 import BeautifulSoup
import requests
# from airflow.operators.latest_only import LatestOnlyOperator

def print_task_3():
    print("Hello World")


def scrapper():

    url = 'https://www.manoramaonline.com/environment/environment-news/2023/03/09/unusual-the-mysterious-rain-of-worms-scares-china.html'
    html_tag = 'h1'
    class_name = "story-headline"

    response = requests.get(url)

    html_content = response.content

    soup = BeautifulSoup(html_content, "html.parser")
    print("soup:", soup)

    title = soup.find(html_tag, class_ = class_name).text
    print("Title of the News is :", title)

    

with DAG(
    dag_id="daily_Scrapper2",
    schedule_interval='@weekly', 
    start_date=dt.datetime(2021, 1, 1),
    catchup=False,
) as dag:
    task1 = EmptyOperator(task_id="task1")
    task2 = EmptyOperator(task_id="task2")
    task3 = PythonOperator(task_id="task3", 
                            python_callable=print_task_3)
    task4 = PythonOperator(task_id="scrapper", 
                            python_callable=scrapper)

    task4 >> [ task3 , task1 ] >> task2
    




    # bin/elasticsearch-users ([useradd <admin>] [-p <admin>] [-r <admin>]) |

