#!/bin/bash

# removes all docker containers even if running
# USAGE: sudo bash ./containers.sh

docker container ls -a > containers

while read -r id _; do
    docker container rm -f $id;
# $1 is the filepath argument
done < containers

rm -f containers
