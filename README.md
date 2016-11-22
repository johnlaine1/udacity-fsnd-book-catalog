# A Book Catalog App

#### Created by: John Laine


## Description
An app that demonstrates the use of Python, Flask, SQLAlchemy and Oauth2 in a simple book catalog application.
Users can log in via Facebook or Google Plus using Oauth2. Only logged in users can create a new book and only the creator of a book can edit or delete that book.

This project was created and submitted to Udacity as part of the Full Stack Developer Nanodegree program.

## Configuring the Application
1. In the config.py file, you will find some app settings, you may have to change these depending on your setup. This app supports both SQLite and PostgreSQL, you can set the database in the config.py file as well, the default is SQLite.
2. In order to setup the Oauth2 authentication, you will need to create a developer acccount at [Facebook](https://developers.facebook.com/) or [Google](https://console.developers.google.com) or both.
3. You will find example configuration files for Facebook and Google Oauth2 in the oauth_credentials folder. After updating the files with your information, remove the .example extension from the filename.

## Running the Application
1. Make sure that you have [Python](https://www.python.org/downloads/) installed.
2. You will also need to install a few modules with `pip install sqlalchemy flask oauth2client requests`
2. Clone the project to your local machine: `https://github.com/johnlaine1/udacity-fsnd-catalog.git`.
3. cd into the project `cd udacity-fsnd-catalog`.
4. Enter `python db_setup.py` to create the database, this will add a file called catalog.db to your system.
5. Enter `python db_populate.py` if you would like to add dummy content to the app (recommended).
6. Enter `python main.py` to start the server.
7. Point your browser to localhost:8080

## Using the Application
1. The front page shows a list of the most recently added books.
2. There is a dropdown menu in the navBar named categories that allows you to sort content by category.
3. If you are logged in, there is also an 'Add a Book' link on the navBar that will allow you to create a new book.
4. You can click on the thumbnail of a book or the 'View' button to see more info about a book.
5. If you are the creator of a book, you will also see 'Edit' and 'Delete' buttons on the thumbnail and book view page.
6. There is a dropdown menu on the navBar named Users that will display links to user bio pages.


## Reviewer Documentation
#### IP = 35.164.131.217
#### SSH Port = 2200
#### URL = http://ec2-35-164-131-217.us-west-2.compute.amazonaws.com
**Software Installed and config changes made**
- Create a new user named grader and grant sudo permission by creating /etc/sudoers.d/grader
- Add the ~/.ssh/authorized_keys file and changed file and folder permissions
- Set the PasswordAuthentication variable in /etc/ssh/sshd_config to no and the Port to 2200
- Use ufw to set and enable firewall: allow ssh, www, ntp, 2200/tcp, deny 22
- Update and Upgrade all packages
- Install apache2, libapache2-mod-wsgi, postgresql, git, pip
- Edited the /etc/apache2/sites-available/000-default.conf file: Added WSGIScriptAlias
- Added the catalog_app.wsgi file to my catalog project
- Ensure that no remote connections are allowed by reviewing /etc/postgresql/9.3/main/pg_hbs.conf
- Create a new db user named 'catalog' that has limited permissions
- Cloned my catalog project in /var/www/catalog_app
- Updated project database settings

**Third party resources used to complete this project**
- https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-14-04
- https://www.digitalocean.com/community/tutorials/how-to-secure-postgresql-on-an-ubuntu-vps
- https://www.a2hosting.com/kb/developer-corner/postgresql/managing-postgresql-databases-and-users-from-the-command-line#Creating-PostgreSQL-databases
- https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
- https://help.ubuntu.com/community/UFW
- http://drumcoder.co.uk/blog/2010/nov/12/apache-environment-variables-and-mod_wsgi/