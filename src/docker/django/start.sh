#!/bin/bash 

# db does not exist error message
db_error="\"django_migrations\" does not exist"

# makemigrations error message
migrate_error="No changes detected"

# create DB migrations
migrations=$(python manage.py makemigrations)

# check if migrations table exists in db
output=$(python manage.py inspectdb django_migrations)

# check if error string is in inspectdb output
if [[ $output == *"$db_error"* ]]; then
    # database does not exist

    # apply DB migrations
    python manage.py migrate

    # create VM users
    python manage.py system data/students.csv

    # create VM mystery objects
    python manage.py mystery data/content

    # assign users to mysteries
    python manage.py assign data/mysteries.csv

    # create VM ta users
    python manage.py ta data/tas.csv

    # create django superuser account
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(username='$SUPER_USER', email=None, password='$SUPER_PASS'); exit()" | python manage.py shell 

    # collect static files
    python manage.py collectstatic

elif [[ $migrations != *"$migrate_error"* ]]; then
    # database exists and new migrations detected

    # apply new migration
    python manage.py migrate

else
    # database exists and no new migrations detected

    # no need to do anything in this state
    true

fi

# copy and load mod_wsgi into apache
mod_wsgi-express install-module > /etc/apache2/mods-enabled/wsgi.load

# start apache
apache2ctl -D FOREGROUND
