FROM python:3.6

# update linux and install apache2
RUN apt-get update && apt-get install -y apache2 apache2-dev && apt-get clean

# copies django application files to /opt
COPY vm-django /opt/vm-django

# copies in python requirements.txt to /opt
COPY Requirements.txt /opt

# changes working directory to /opt
WORKDIR /opt

# install and create a python virtual environment
RUN pip3.6 install virtualenv && virtualenv --python=/usr/local/bin/python3.6 djangoenv

# run the rest of the commands in the virtual environment
WORKDIR djangoenv/bin
RUN /bin/bash -c "source activate"

# install python packages
WORKDIR /opt
RUN pip3.6 install -r Requirements.txt && pip3.6 install mod_wsgi && pip3.6 install django-storages && pip3.6 install boto3

# Change into django project directory
WORKDIR /opt/vm-django

# Copy django startup script
COPY /docker/django/start.sh .

# Copy wait-for-it script
COPY /docker/django/wait-for-it.sh .

# give permission to execute start.sh and django files
RUN chmod +x start.sh && chmod o+x /opt

# copies apache .conf files
COPY docker/django/000-default.conf /etc/apache2/sites-enabled/000-default.conf
COPY docker/django/000-default.conf /etc/apache2/sites-available/000-default.conf



