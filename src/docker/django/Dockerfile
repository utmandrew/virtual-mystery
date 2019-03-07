FROM python:3.6

# update linux
RUN apt-get update

# install apache2
RUN apt-get install -y apache2 apache2-dev

# copies django application files to /opt
COPY vm-django /opt/vm-django

# copies virtual mystery data files to /opt/vm-django
COPY data/vm-data /opt/vm-django/data

# copies in python requirements.txt to /opt
COPY Requirements.txt /opt

# changes working directory to /opt
WORKDIR /opt

# install python virtual environment
RUN pip3.6 install virtualenv

# make a virtual environment
RUN virtualenv --python=/usr/local/bin/python3.6 djangoenv

# run the rest of the commands in the virtual environment
WORKDIR djangoenv/bin
RUN /bin/bash -c "source activate"

# install python packages
WORKDIR /opt
RUN pip3.6 install -r Requirements.txt
RUN pip3.6 install mod_wsgi

# Change into django project directory
WORKDIR /opt/vm-django

# Copy django startup script
COPY /docker/django/start.sh .

# Copy wait-for-it script
COPY /docker/django/wait-for-it.sh .

# give permission to execute
RUN chmod +x start.sh

# give apache executable permissions to the django file dir
RUN chmod o+x /opt

# copies apache .conf files
COPY docker/django/000-default.conf /etc/apache2/sites-enabled/000-default.conf
COPY docker/django/000-default.conf /etc/apache2/sites-available/000-default.conf



