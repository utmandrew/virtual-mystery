#!/bin/bash

# removes all docker images
# USAGE: sudo bash ./images.sh

docker image ls -a > images

while read -r _ _ id _; do
    docker image rm -f $id;
# $1 is the filepath argument
done < images

rm -f images
