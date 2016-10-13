# A Book Catalog App

#### Created by: John Laine


## Description
An app that demonstrates the use of Python, Flask, SQLAlchemy and Oauth2 in a simple book catalog application.
Users can log in via Facebook or Google Plus using Oauth2. Only logged in users can create a new book and only the creator of a book can edit or delete that book.

This project was created and submitted to Udacity as part of the Full Stack Developer Nanodegree program.

## Configuring the Application
1. In the config.py file, you will find 'host' and 'port' settings, you may have to change these depending on your setup.
2. In order to setup the Oauth2 authentication, you will need to create a developer acccount at [Facebook](https://developers.facebook.com/) or [Google](https://console.developers.google.com) or both.
3. You will find example configuration files for Facebook and Google Oauth2 in the oauth_credentials folder. After updating the files with your information, remove the .example from the filename.

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