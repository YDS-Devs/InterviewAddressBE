#!/bin/bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py loaddata countries.json
python3 manage.py loaddata states.json
python3 manage.py loaddata areas.json
python3 manage.py runserver