# Django containerized app
Template of containerized Django application.

## Features:
- `docker-compose.yml` for fast running component (running with or without database).
- `docker-compose.test.yaml` for tests running.
- Working connection to `MySQL`.
- `SQLite` for running tests with database.
- Logging in json format supporting Logstash.

## Usage
Using docker-composer:
~~~bash
docker-compose build
docker-compose up
~~~

## Urls
- Admin UI (login: `admin`, `passwd`): <http://localhost:8000>
- Custom web page: <http://localhost:8000/static>
- HTTP interface: <http://localhost:8000/samples>
- Metrics for Prometheus: <http://localhost:8000/metrics>

## Run tests
~~~bash
docker-compose -f docker-compose.test.yml build
docker-compose -f docker-compose.test.yml up
~~~
