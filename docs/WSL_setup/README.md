This guide will go through setting up Virtual Mystery on a Windows machine from scratch.

Requirements:
    Windows 10 version 2004, build 19041 or higher.
    Open command prompt and type `ver` to check this.

    C:\Users\haoch>ver

    Microsoft Windows [Version 10.0.19041.508]

1. **Enabling WSL**  
     Go to `Control Panel` > `Programs` > `Programs and Features` > `Turn Windows features on or off`.  
     Enable `Windows Subsystem for Linux` and `Virtual Machine Platform`.  
     Click OK and restart your PC.

2. **Setting WSL to version 2**  
     Open Windows PowerShell and run the command `wsl --set-default-version 2`.  
     You might get a message that says `"WSL 2 requires an update to its kernel component."`.  
     If you get the above message, follow the link and download and run the kernel installer,
     then run the wsl command again.

3. **Installing Ubuntu**  
     Go to the Microsoft Store and install `Ubuntu 20.04 LTS` from `Canonical Group Limited`.  
     Launch the app and set up a user account with your desired username and password.  
     Run `sudo apt-get update`.  
     Run `sudo apt-get upgrade` and confirm the command.

4. **Installing pip**  
     Open Ubuntu and run `sudo apt install python3-pip`.

5. **Installing virtualenvs**  
     Run `sudo pip3 install virtualenv`.  
     Run `sudo pip3 install virtualenvwrapper`.

6. **Installing postgresql**  
     Run `sudo apt-get install postgresql`.

7. **Creating a postgres database**  
     First, start `postgres` by running `sudo service postgresql start`.  
     Enter the postgres shell by running `sudo -u postgres psql`.  
     You should see your shell prompt change to `postgres=#`.

     Now run the following commands:  
     (The capitalization, quotation marks, and semicolons are important)

     ```
     CREATE USER <username> WITH PASSWORD '<password>';
     ALTER USER <username> CREATEDB;
     CREATE DATABASE <database name> OWNER <username>;
     ```

     Type `\l` to ensure that the database you specified has been created.

     Your shell should look like this, albeit with different names and passwords:
     ```
     postgres=# CREATE USER usr WITH PASSWORD 'usr';
     CREATE ROLE
     postgres=# ALTER USER usr CREATEDB;
     ALTER ROLE
     postgres=# CREATE DATABASE vmdb OWNER usr;
     CREATE DATABASE
     postgres=# \l
                                   List of databases
        Name    |  Owner   | Encoding | Collate |  Ctype  |   Access privileges
     -----------+----------+----------+---------+---------+-----------------------
      postgres  | postgres | UTF8     | C.UTF-8 | C.UTF-8 |
      template0 | postgres | UTF8     | C.UTF-8 | C.UTF-8 | =c/postgres          +
                |          |          |         |         | postgres=CTc/postgres
      template1 | postgres | UTF8     | C.UTF-8 | C.UTF-8 | =c/postgres          +
                |          |          |         |         | postgres=CTc/postgres
      vmdb      | usr      | UTF8     | C.UTF-8 | C.UTF-8 |
     (4 rows)
     ```

     Type `\q` to exit the postgres shell.

8. **Activating virtualenvwrapper**  
     You'll find that the `virtualenvwrapper` commands don't actually run yet,
     so add these lines to the end of your `.bashrc` file located in your home directory:

     ```
     export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
     export WORKON_HOME=~/.virtualenvs
     source /usr/local/bin/virtualenvwrapper.sh
     ```

     After saving the `.bashrc` file, restart Ubuntu for the changes to take effect.

9. **Creating a virtual environment**  
     In your home directory, make a virtual environment for the project.  
     This can be done by running `mkvirtualenv -p <python version> <virtual environment name>`.  
     e.g. `mkvirtualenv -p python3 vmenv`.

     To enter this virtual environment in the future, run `workon <environment name>`.
     e.g. `workon vmenv`.

     When you are in the virtual environment, your shell prompt should
     have a prefix that is the name of that environment, like so:
     `(vmenv) hhc@HHC-PC:~$`

10. **Clone the git repo**  
     Run `git clone git@github.com:utmandrew/virtual-mystery.git` to clone the repo into
     a desired directory.

11. **Install Requirements**  
     In Ubuntu, navigate to the repo you just cloned and go into the `src` folder.
     You should see a file named `Requirements.txt`.  
     If you cloned the repo into your Windows file system, this can be done by
     holding down the shift key, right clicking, and selecting `Open Linux shell here`
     from the dropdown menu within file explorer.

     Once in the repo, make sure you are still working on your virtual environment,
     run `workon <environment name>` if that's not the case.

     Inside the virtual environment, `pip` is mapped to `pip3`, so we can start using `pip` instead.  
     Run `sudo apt-get install libpq-dev`. This is a required library for one of the packages.  
     Run `pip install -r Requirements.txt` and ensure no errors are thrown.  
     Run `pip install mod-wsgi-httpd`, this will take a while.  
     Run `pip install mod-wsgi`.

     Once you are done those steps, make sure you have everything installed correctly by
     running `pip freeze`.
     For reference, the package versions used for this guide are:
     ```
     Python 3.8.2
     asgiref==3.2.10
     bleach==3.1.5
     chardet==3.0.4
     Django==3.0.7
     django-cors-headers==3.4.0
     djangorestframework==3.11.0
     Markdown==3.2.2
     mod-wsgi==4.7.1
     mod-wsgi-httpd==2.4.41.1
     packaging==20.4
     psycopg2==2.8.5
     pyparsing==2.4.7
     pytz==2020.1
     six==1.15.0
     sqlparse==0.3.1
     webencodings==0.5.1
     ```

12. **Configure Django settings.py file**
     - navigate to `virtual-mystery/src/vm-django/VM_Django`
     - open up the `settings.py` file in a text editor
     - set `DEBUG = False`
     - Change database settings:
        - Note: single quotes are required
        - `NAME` = database name (name of created db in postgres)
        - `USER` = database owner username
        - `PASSWORD` = database owner password
        - `HOST` = can be left as localhost
        - `PORT` = 5432 (default postgresql port)
     - Change CORS settings:
        - comment out `CORS_ORIGIN_ALLOW_ALL = True`
        - uncomment `CORS_ORIGIN_WHITELIST`
        - add server ip to the whitelist (again, not recommended to include a port)

13. **Setup Django (in virtual environment)**  
     Navigate to `virtual-mystery/src/vm-django`.  
     Run `python manage.py makemigrations`.  
     Run `python manage.py migrate`.  
     Run `python manage.py createsuperuser`.  
     Enter preferred credentials when prompted (skip email field by pressing enter if desired).  
     A `Superuser created successfully.` prompt should be shown afterwards.  
     Run `python manage.py collectstatic`.

14. **Install apache2 and Angular**  
     *apache2*:  
     Run `sudo apt install apache2`.

     *Angular*:  
     Run `sudo apt install npm` for the package manager to install Angular.  
     Run `sudo npm install npm@latest -g`, and RESTART Ubuntu. **(IMPORTANT!)**  
     Run `sudo npm install -g n`.  
     Run `sudo n 12.16.3` to get the right node version.  
     Run `sudo npm install -g @angular/cli` to install Angular.

15. **Building Angular**  
     Navigate to `virtual-mystery/src/vm-angular`.  
     Run `sudo npm install`, this takes a while.  
     Run `ng build --prod`, this also takes a while, and will produce a `dist` folder.  
     Link to the `dist` folder correctly in your `.conf` file.

16. **Setting up the site**  
     Navigate to `/etc/apache2/sites-available` and add your `.conf` file there.  
     Run `sudo apt-get install libapache2-mod-wsgi-py3`.  
     Run `sudo a2enmod wsgi`.  
     Run `sudo a2enmod proxy`.  
     Run `sudo a2enmod proxy_http`.  
     Run `sudo a2enmod rewrite`.  
     Run `sudo a2dissite 000-default`.  
     Run `sudo a2ensite <your site (conf file) name>`.

     Note: this step will determine whether the site runs or not, but unfortunately
     the setup differs for every system. Make sure your `.conf` file links to the correct
     files and grants appropriate access permissions. Sample files will be provided in this directory.

17. **Testing the site**  
     Restart `apache2`, and ensure that `postgres` is running.  
     Your site should now be set up, test it by accessing `localhost` and
     verifying that the login page displays. Go to `localhost/admin` and verify
     that the django login page displays. Try to log in.

18. **Adding content**  
     The site should now be set up. To add content and actually be able to log in, follow the instructions
     in [Setup.txt](https://github.com/utmandrew/virtual-mystery/blob/master/docs/Setup.txt "Setup documentation").
