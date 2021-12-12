from datetime import datetime, timedelta, time
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.sensors.time_sensor import TimeSensorAsync
from airflow.sensors.time_delta import TimeDeltaSensorAsync



# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}
with DAG(
    'defferable_dag',
    default_args=default_args,
    description='Defferable Dag',
    schedule_interval=None,
    start_date=days_ago(2),
    tags=['custom'],
) as dag:
    dag.doc_md = """
# Defferable Tasks example
This dag demonstrates the usage of defferable tasks. Take a look at task async_wait (third task) and compare it with
the execution of the second task, which uses the old approach of waiting within the worker.
"""

    # t1, t2 and t3 are examples of tasks created by instantiating operators
    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    t2 = BashOperator(
        task_id='sleep',
        bash_command='sleep 2',
        retries=3,
    )
    t3 = TimeDeltaSensorAsync(
        task_id="async_wait",
        delta=timedelta(seconds=20)
    )
    t4 = BashOperator(
        task_id="echo_success",
        bash_command="echo success"
    )

    t2 >> t3 >> t4
