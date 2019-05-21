# Airflow Libraries:
import airflow
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from utils import pull_api_data

args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(7),
    'provide_context': True  # Allows us to get execution properties
}

dag = airflow.DAG(
    'scada_stg1_pull',
    schedule_interval="@daily",
    dagrun_timeout=timedelta(minutes=60),
    default_args=args,
    max_active_runs=1)

etl_start = BashOperator(
task_id='etl_start',
bash_command='echo "STARTING ETL RUN:"',
dag=dag)


pull_api_data = PythonOperator(
    task_id='pull_api_data',
    python_callable=pull_api_data,
    op_kwargs={ 'start_time': '2019-01-01 00:00:00',
                'end_time': '2019-01-02 00:00:00',
                'server_name': 'ewis-battne',
                'tag_name': 'BPB_BATTxxx_SUB0001_Revenue_Meter_MWH_Rec'
    },
    dag=dag
)


etl_stop = BashOperator(
task_id='etl_stop',
bash_command='echo "COMPLETED ETL RUN:"',
dag=dag)


etl_start.set_downstream(pull_api_data)
pull_api_data.set_downstream(etl_stop)
