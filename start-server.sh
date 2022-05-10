#!/usr/bin/env bash
(cd mysite; python manage.py makemigrations; python manage.py migrate)
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd mysite; python manage.py createsuperuser --no-input)
fi
(cd mysite; gunicorn mysite.wsgi:application --bind 0.0.0.0:$PORT --workers 3)