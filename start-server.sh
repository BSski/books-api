#!/usr/bin/env bash
(cd api; python manage.py makemigrations; python manage.py migrate;
  python manage.py collectstatic --no-input)

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
  (cd api; python manage.py createsuperuser --no-input)
fi
(cd api; gunicorn api.wsgi:application --bind 0.0.0.0:$PORT --workers 3)