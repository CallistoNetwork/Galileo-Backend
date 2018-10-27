#!/usr/bin/env bash

python manage.py migrate --settings=galileo.settings.prod
python manage.py collectstatic --settings=galileo.settings.prod --noinput

gunicorn -w 2 galileo.wsgi:application -b 0.0.0.0:8000  --log-level info --keep-alive 200 --env DJANGO_SETTINGS_MODULE=galileo.settings.prod
