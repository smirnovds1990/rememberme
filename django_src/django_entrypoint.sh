#!/bin/sh
uv run manage.py migrate --noinput
uv run manage.py runserver ${HOST}:${PORT}
