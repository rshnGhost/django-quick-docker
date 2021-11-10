#!/bin/sh

set -e

#whoami

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate

#pwd
#ls -la
#ls -la /vol/
#ls -la /vol/web/static
#ls -la /vol/Files/staticFile
#ls -la /vol/Files/staticFile
#ls -la /vol/web/static

uwsgi --socket :9000 --workers 4 --master --enable-threads --module main.wsgi
