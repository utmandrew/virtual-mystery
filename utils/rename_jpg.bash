#!/bin/bash

for i in $(find . -iname "*.JPG"); do
    git mv "$i" "$(echo $i | rev | cut -d '.' -f 2- | rev).jpg";
done
