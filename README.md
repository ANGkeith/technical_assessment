# Technical Test

## Installation

Change directory into the directory that contains docker-compose.yml and start the container with:

```
docker-compose up
```

The database will be in a clean state.

###  Initialize database
Currently, the database is not popuated. The following code is used to initialize the database with some values. 
```
docker-compose exec app sh -c 'source script/init_db.sh'
```
This will create a User with the following:
```
username: admin
password: admin
```
And also populate the database with the data from `\app\script\data\`

### Periodic task
I am unable to integrate this into docker-compose. Thus, had to make do with this solution. On another terminal, run the
following code to start the celery periodic task

```
docker-compose exec app sh
celery -A app beat -q &
celery -A app worker --loglevel=info
```
Head over to http://localhost:8000/api/doctype-datas/Email/ and the total_docs should increment around every 10s

In this terminal, it will also show the number of files in the `/app/media/Files` directory every 5s


### Unit test
This can be used to run the unit test which mainly only validating on the api responses.
```
docker-compose exec app sh -c 'python manage.py test'
```



## Usage
Go to your favourite web browser and key in http://localhost:8000/api/ to view the various end point.

## Requirements
Docker version 18.09.2, build 6247962


## Uninstall
```
docker rm -f technical_assessment_app_1 technical_assessment_db_1 technical_assessment_rabbitmq_1
docker volume rm -f technical_assessment_postgres_data
docker image rm technical_assessment_app:latest technical_assessment_celery_worker:latest postgres rabbitmq

```
