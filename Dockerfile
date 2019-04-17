FROM python:3.7.0-stretch

RUN apt-get update && apt-get install --yes \
      mysql-client \
      default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/* && \
    pip install django==2.1.2 \
                django-prometheus==1.0.15 \
                django-rest-swagger==2.2.0 \
                djangorestframework==3.9.2 \
                pytest-django==3.4.8 \
                dj-static==0.0.6 \
                pytz==2018.3 \
                gunicorn==19.9.0 \
                mysqlclient==1.3.13 \
                logstash_formatter==0.5.17

RUN mkdir /app

COPY app                            /app/app
COPY django_server                  /app/django_server
COPY job                            /app/job
COPY tests                          /app/tests
COPY setup.py                       /app/
COPY manage.py                      /app/
COPY scripts/migrate.sh             /app/
COPY scripts/run_web.sh             /app/
COPY scripts/run_job.sh             /app/

RUN cd /app && \
    pip install .

EXPOSE 8000

CMD ["/app/run_web.sh"]
