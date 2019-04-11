#!bin/bash

# This creates a admin account and populate the db with the data

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@dathena.com', 'admin')" | python /app/manage.py shell

python /app/script/init_db.py
