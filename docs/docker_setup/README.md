This guide will go through deploying Virtual Mystery via docker from a fresh Ubuntu/WSL2 install, similar to what was done in the [WSL_setup](https://github.com/utmandrew/virtual-mystery/tree/master/docs/WSL_setup "WSL setup documentation") documentation.

1. **Installing docker-cli**  
    **Do not** do this through `apt` or `apt-get`.  
    Instead, follow the instructions [here](https://docs.docker.com/engine/install/ubuntu/ "Docker Ubuntu setup") to set up docker.

2. **Installing docker-compose**  
    At the time of writing of this guide, `docker-compose` does not come with the installation of `docker`. So we need to install it separately. Follow the `Linux` instructions [here](https://docs.docker.com/compose/install/ "Docker Ubuntu setup") to set up `docker-compose`.

3. **Make sure nothing is running on port 443**  
    As title, because the apache instance in docker binds to port 443.
