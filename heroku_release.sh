#!/bin/sh

pip install -r requirements.txt -r requirements_heroku.txt
python manage.py migrate
