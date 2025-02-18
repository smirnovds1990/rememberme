#!/bin/sh
uv run manage.py collectstatic --noinput
uv run manage.py migrate --noinput
uv run gunicorn rememberme.wsgi:application --bind ${HOST}:${PORT}
