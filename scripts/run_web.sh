#!/bin/bash

if [[ "$USE_DB" == "1" ]]; then
    # run db migrations if needed
    /app/migrate.sh
fi

cd /app

python manage.py collectstatic --noinput

exec gunicorn django_server.wsgi:application \
                        --name django_server \
                        --bind 0.0.0.0:8000 \
                        --access-logfile - \
                        --error-logfile - \
                        --workers 2 \
                        --log-level info \
                        "$@"
