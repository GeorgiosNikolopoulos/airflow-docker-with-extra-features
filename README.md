# Docker deployment of airflow with extra features
This git repo contains all required files and configurations to run airflow 2.2.2 with celery, postgres and redis.
Additionally, some extra features are enabled:
1) Grafana and prometheus integration via statsd-exporter (extra containers are run for this)
2) Sentry support
3) Remote log writing to azure support
4) Plugin support in folder plugins with examples
5) Debug mode on worker for extra information

The main file to examine is docker-compose.yaml. It contains all the configuration needed to run airflow with these extra
features. The most critical parts are at the top, which houses the Environment variables passed to the airflow containers.

To run:
1. Docker is required 
2. execute 'docker-compose build' to create the local images
3. Execute 'docker-compose up' to start the entire deployment and see all logs. You can add -d (docker-compose up -d) to run in detacched mode.


URLS (with username - password):  
Airflow: http://localhost:8080/ airflow airflow  
Grafana: http://localhost:3000/login admin admin  
Prometheus: http://localhost:9090/ no auth  
Flower: http://localhost:5555/ no auth  

To terminate and delete containers:  
Cntrl+C if running without -d option  
'docker-compose down' to delete containers.

If you wish to reset the entire deployment run the reset.sh file in the root airflow folder. You must then rebuild and relaunch.

If you want to set up remote logs, follow these steps:
1. Set up an azure storage account
2. Create a container called airflow-logs
3. Set up the connection in airflow (Microsoft azure blob storage type). Easiest way to do this is via a Connection String (Availabe in the access key section of the storage acount).
You can give it any name but the docker-compose file uses az-logs
4. Change the AIRFLOW__LOGGING__REMOTE_LOGGING boolean in the compose file to true

For sentry:
1. set up an account with sentry (DEV type, free)
2. Change AIRFLOW__SENTRY__SENTRY_ON to true
3. Add the DNS address for your account to AIRFLOW__SENTRY__SENTRY_DSN

