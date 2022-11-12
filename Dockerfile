FROM apache/airflow:2.3.0-python3.9

RUN pip install 'apache-airflow[sentry]'

CMD ["airflow", "standalone"]