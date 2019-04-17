#!/bin/bash

cd /app

python manage.py migrate

# Create django app superuser. This will be done only once, if no 'admin' user exists.
python manage.py shell -c "from django_server.utils import try_create_admin_user; try_create_admin_user()"
