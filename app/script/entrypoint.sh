#!/bin/bash
# taken from https://medium.com/@kenanbek/configure-docker-compose-startup-order-for-django-rest-framework-and-celery-rabbitmq-redis-127f7a482626
# python manage.py test
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
exec "$@"
