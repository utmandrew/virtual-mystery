The contents of this folder are mounted into the django container and holds the migrations for each django app respectively. 

NOTE: 
 - The contents within the migrations folder for each django app will be replaced (masked) by the contents within thier respective migrations folder contained in this directory.
 - Ensure that all migrations folders contain, at a minimum, an empty file named __init__.py
 - Copy over the migrations folder contents for each django app into thier respective migrations folders in this directory before initial docker container startup.  
 
