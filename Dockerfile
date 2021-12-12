FROM apache/airflow:2.2.2-python3.8

RUN pip install 'apache-airflow[sentry]'

CMD ["airflow", "standalone"]