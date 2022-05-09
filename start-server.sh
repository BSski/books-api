#!/usr/bin/env bash
(cd booksapi; python manage.py makemigrations; python manage.py migrate)
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd booksapi; python manage.py createsuperuser --no-input)
fi
(cd booksapi; gunicorn movies.wsgi:application --bind 0.0.0.0:$PORT --workers 3)