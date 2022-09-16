#!/bin/sh
# Exit immediately if a command exits with a non-zero status.
# http://stackoverflow.com/questions/19622198/what-does-set-e-mean-in-a-bash-script
set -e

case "$1" in
    admin)
        export DEBUG=True
        export ADMIN=True
        python3 manage.py migrate --noinput
        python3 manage.py collectstatic --noinput
        exec gunicorn simple_tasks.wsgi -b 0.0.0.0:8000 -w 2
    ;;
    web)
        export DEBUG=True
        export ADMIN=True
        python3 manage.py migrate --noinput
        python3 manage.py collectstatic --noinput

        exec gunicorn simple_tasks.wsgi -b 0.0.0.0:8000 -w 4
    ;;

esac
