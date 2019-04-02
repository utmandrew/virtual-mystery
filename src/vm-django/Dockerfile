FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y apache2 apache2-dev && apt-get clean
RUN mkdir /code
WORKDIR /code
RUN mkdir /vm-django
RUN pip3.6 install virtualenv && virtualenv --python=/usr/local/bin/python3.6 djangoenv
WORKDIR djangoenv/bin
RUN /bin/bash -c "source activate"
WORKDIR /code
COPY Requirements.txt /code/vm-django
WORKDIR /vm-django/
COPY . .
RUN pip install -r Requirements.txt && pip3.6 install mod_wsgi
