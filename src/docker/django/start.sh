#!/bin/bash

# create DB migrations
python manage.py makemigrations

# apply DB migrations
python manage.py migrate

# create VM users
python manage.py system data/students.csv

# create VM mystery objects
python manage.py mystery data/content

# assign users to mysteries
python manage.py assign data/mysteries.csv

# collect static files
python manage.py collectstatic

# copy and load mod_wsgi into apache
mod_wsgi-express install-module > /etc/apache2/mods-enabled/wsgi.load

# start apache
apache2ctl -D FOREGROUND
