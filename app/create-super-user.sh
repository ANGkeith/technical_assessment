echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@dathena.com', 'admin')" | python manage.py shell
