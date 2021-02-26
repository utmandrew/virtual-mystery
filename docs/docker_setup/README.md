This guide will go through deploying Virtual Mystery via docker from a fresh Ubuntu/WSL2 install,
similar to what was done in the [WSL_setup](https://github.com/utmandrew/virtual-mystery/tree/master/docs/WSL_setup "WSL setup documentation") documentation.  
Keep in mind that this guide assumes you've installed all the utilities needed in the previous guide.

1. **Installing docker-cli**  
    **Do not** do this through `apt` or `apt-get`.  
    Instead, follow the instructions [here](https://docs.docker.com/engine/install/ubuntu/ "Docker Ubuntu setup") to set up docker.

2. **Installing docker-compose**  
    At the time of writing of this guide, `docker-compose` does not come with the installation of `docker`. So we need to install it separately. Follow the `Linux` instructions [here](https://docs.docker.com/compose/install/ "Docker compose setup") to set up `docker-compose`.

3. **Make sure nothing is listening on port 443**  
    As title, because the apache instance in docker binds to port 443.

4. **Copy in content**  
    Copy in the mystery contents into `virtual-mystery/src/data/vm-data` with the contents formatted according to the [readme](https://github.com/utmandrew/virtual-mystery/blob/master/src/data/vm-data/readme.txt "contents readme").

5. **Copy in SSL certificates**  
    Obtain SSL certificates for the domain you will be hosting Virtual Mystery on, and copy those certificates into `virtual-mystery/src/data/ssl`. The [readme](https://github.com/utmandrew/virtual-mystery/blob/master/src/data/ssl/readme.txt "ssl certificates readme") has more information about the types of certificates needed.

6. **Building Angular**  
    Navigate to `virtual-mystery/src/vm-angular`.  
    Run `sudo npm install`, this takes a while.  
    Run `ng build --prod`, this also takes a while, and will produce a `dist` folder.

7. **Start up the containers**  
    Make sure docker is running, you can start it by running the command `sudo service docker start`.  
    `cd` to `virtual-mystery/src` and run `sudo docker-compose up --build -d` and the website should begin building.

8. **Change permissions on log files**  
    Navigate to `virtual-mystery/src/vm-django/logs` and run `chmod 622 activity.log debug.log`.  
    This will enable the container to write to the log files on the host file system.

### Miscellaneous tips
1. Enter the django container by running `sudo docker exec -it src_django_1 bash`.  
    The apache logs are located at `/var/log/apache2` within the container, for when you need to debug any issues.
