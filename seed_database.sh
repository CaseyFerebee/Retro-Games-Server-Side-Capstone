#!/bin/bash

rm db.sqlite3
rm -rf ./retroapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations retroapi
python3 manage.py migrate retroapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata conditions
python3 manage.py loaddata genres
python3 manage.py loaddata games
python3 manage.py loaddata owners
python3 manage.py loaddata game_collection
python3 manage.py loaddata controllers
python3 manage.py loaddata controller_collection
python3 manage.py loaddata consoles
python3 manage.py loaddata console_collection