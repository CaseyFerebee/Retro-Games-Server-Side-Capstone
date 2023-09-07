#!/bin/bash

rm db.sqlite3
rm -rf ./retroapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations retroapi
python3 manage.py migrate retroapi
python3 manage.py loaddata condition
python3 manage.py loaddata tokens
python3 manage.py loaddata console
python3 manage.py loaddata controller
python3 manage.py loaddata genre
python3 manage.py loaddata owner
python3 manage.py loaddata users