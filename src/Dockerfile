# all the python stuff
FROM python:3

#python env 
ENV PYTHONUNBUFFERED 1

# create a directory to work in for the project
RUN mkdir /virtual-mystery
WORKDIR /virtual-mystery

# at this point the container doesn't have anything
# It only has python:3 and the environment stuff
# now we copy the code "all the code in 'src' ...I think"
COPY . /virtual-mystery/


# install all the requirements fromt he 
# Requirements file from the parent directory
RUN pip install -r ../Requirements.txt

