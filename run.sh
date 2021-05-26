#!/bin/bash

python manage.py migrate

uwsgi --http 0.0.0.0:8000 --module config.wsgi --workers 32 --threads 4
